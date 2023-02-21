from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import (Team,
                     TeamPost,
                     CommentTeamPost,
                     Invite,
                     SubscribersTeam,
                     )

from .serializers import (ListTeamViewSerializers,
                          RetrieveTeamViewSerializers,
                          ListPostTeamViewSerializers,
                          RetrieveEditUserPostSerializers,
                          EditDestroyViewSerializers,
                          TeamCreateSerializers,
                          AddPostTeamSerializers,
                          RetrievePostTeamSerializers,
                          CommentsCreateTeamPostSerializers,
                          CommentsListTeamPostSerializers,
                          CommentsRetDesUpTeamPostSerializers,
                          CreateInviteSerializers, ListSubscribersSerializers, DeleteSubscribersSerializers,
                          )

from base.classes import MixedPermission

from base.permissions import IsUser, IsUserTeam, IsUserInPost, IsAuthorTeam, IsAuthorObjTeam


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


class ListSubscribersView(generics.ListAPIView):
    serializer_class = ListSubscribersSerializers
    permission_classes = (IsUserTeam, )

    def get_queryset(self):
        return SubscribersTeam.objects.filter(team_id=self.kwargs.get('pk'))


class DelFollowingTeamView(MixedPermission, viewsets.ModelViewSet):
    queryset = SubscribersTeam.objects.all()
    serializer_class = DeleteSubscribersSerializers
    permission_classes_by_action = {
        'retrieve': (IsUserTeam,),
        'update': (IsAuthorTeam,),
        'destroy': (IsAuthorObjTeam, ),
    }
    lookup_url_kwarg = 'num_user_fol'


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
        'create': (IsAuthorTeam, ),
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


class AddCommentsTeamPostView(viewsets.ModelViewSet):
    queryset = CommentTeamPost.objects.all()
    serializer_class = CommentsCreateTeamPostSerializers
    permission_classes_by_action = {
        'create': (IsUserTeam,),
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, comment_team_post_id=self.kwargs.get('num_post'))


class ListCommentsTeamPostView(generics.ListAPIView):
    serializer_class = CommentsListTeamPostSerializers

    def get_queryset(self):
        return CommentTeamPost.objects.filter(comment_team_post_id=self.kwargs.get('num_post'))


class RetUpDesCommentsTeamPostView(MixedPermission, viewsets.ModelViewSet):
    queryset = CommentTeamPost.objects.all()
    serializer_class = CommentsRetDesUpTeamPostSerializers
    permission_classes_by_action = {
        'retrieve': (IsAuthenticatedOrReadOnly,),
        'update': (IsUser,),
        'destroy': (IsUserInPost, ),
    }
    lookup_url_kwarg = 'num_comment'


class CreateInviteTeamView(generics.CreateAPIView):
    queryset = Invite.objects.all()
    serializer_class = CreateInviteSerializers
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, team_id=self.kwargs.get('pk'))


# class DelInviteTeamView(generics.DestroyAPIView):
#     serializer_class = CreateInviteSerializers
#     permission_classes = (IsAuthenticated, )

