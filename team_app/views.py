from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import Team, TeamPost
from .serializers import (ListTeamViewSerializers,
                          RetrieveTeamViewSerializers,
                          ListPostTeamViewSerializers,
                          RetrieveEditUserPostSerializers,
                          EditDestroyViewSerializers, TeamCreateSerializers, AddPostTeamSerializers,
                          RetrievePostTeamSerializers,
                          )
from base.classes import MixedPermission

from base.permissions import IsUser, IsUserTeam


class ListTeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = ListTeamViewSerializers


class CreateTeamView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamCreateSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RetrieveTeamView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = RetrieveTeamViewSerializers


class AddDelFollowingTeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = RetrieveTeamViewSerializers
    permission_classes = (IsAuthenticated, )

    @action(detail=True, methods=['put', ])
    def add_del_following(self, request, pk):
        follower = self.get_object()
        if self.request.user in follower.subscribers.all():
            follower.subscribers.remove(self.request.user)
        else:
            follower.subscribers.add(self.request.user)
        return Response(status=201)


class TeamEditRetrieveUpdateDestroyView(MixedPermission, viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = EditDestroyViewSerializers
    permission_classes_by_action = {
        'retrieve': (IsAuthenticatedOrReadOnly,),
        'update': (IsUser,),
        'destroy': (IsUser,),
    }


class ListPostTeamView(generics.ListAPIView):
    serializer_class = ListPostTeamViewSerializers

    def get_queryset(self):
        return TeamPost.objects.filter(team_post_id=self.kwargs.get('pk'))


class AddPostTeamView(MixedPermission, viewsets.ModelViewSet):
    queryset = TeamPost.objects.all()
    serializer_class = AddPostTeamSerializers
    permission_classes_by_action = {
        'create': (IsUserTeam, ),
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, team_post_id=self.kwargs.get('pk'))


class RetrieveEditUserPostView(MixedPermission, viewsets.ModelViewSet):
    queryset = TeamPost.objects.all()
    serializer_class = RetrieveEditUserPostSerializers
    permission_classes_by_action = {
        'retrieve': (IsAuthenticatedOrReadOnly,),
        'update': (IsUser,),
        'destroy': (IsUser,),
    }
    lookup_url_kwarg = 'num_post'


class AddLikesOrDislikesTeamPostView(viewsets.ModelViewSet):
    queryset = TeamPost.objects.all()
    serializer_class = RetrievePostTeamSerializers
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'num_post'

    @action(detail=True, methods=('put',))
    def set_like(self, request, pk, num_post):
        post = self.get_object()
        print(post)
        if self.request.user in post.dislikes.all():
            post.dislikes.remove(self.request.user)
        if self.request.user in post.likes.all():
            post.likes.remove(self.request.user)
        else:
            post.likes.add(self.request.user)
        return Response(status=201)

    @action(detail=True, methods=['put'])
    def set_dislike(self, request, pk, num_post):
        post = self.get_object()
        if self.request.user in post.likes.all():
            post.likes.remove(self.request.user)
        if self.request.user in post.dislikes.all():
            post.dislikes.remove(self.request.user)
        else:
            post.dislikes.add(self.request.user)
        return Response(status=201)
