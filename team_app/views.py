from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .service import ListTeamFilter
from .models import (
    Team,
    TeamPost,
    CommentTeamPost,
    Invite,
    SubscribersTeam,
)

from .serializers import (
    ListTeamViewSerializers,
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
    InviteSerializers,
    ListSubscribersSerializers,
    DeleteSubscribersSerializers,
    ListInviteTeamSerializers,
    RetrieveInviteSerializers,
    UpdateInviteSerializers,
)

from base.classes import MixedPermission, MixedSerializer

from base.permissions import (
    IsUser,
    IsUserTeam,
    IsUserInPost,
    IsAuthorTeam,
    IsInvite,
    IsAdminTeam,
    IsUserInPostTeam,
)


class ListTeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = ListTeamViewSerializers
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ListTeamFilter

    def get_queryset(self):
        return Team.objects.select_related('category').prefetch_related('stack').all()


class CreateTeamView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamCreateSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RetrieveTeamView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = RetrieveTeamViewSerializers

    def get_object(self):
        obj = Team.objects.select_related('user', 'category').prefetch_related('stack').get(id=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj


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
        'destroy': (IsAuthorTeam, ),
    }

    def get_object(self):
        obj = SubscribersTeam.objects.select_related('user', 'team', ).get(id=self.kwargs.get('num_user_fol'))
        self.check_object_permissions(self.request, obj)
        return obj


class TeamEditRetrieveUpdateDestroyView(MixedPermission, viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = EditDestroyViewSerializers
    permission_classes_by_action = {
        'retrieve': (IsAuthenticatedOrReadOnly,),
        'update': (IsUser,),
        'destroy': (IsUser,),
    }

    def get_object(self):
        obj = Team.objects.select_related('category', 'user').prefetch_related('stack').get(id=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj


class ListPostTeamView(generics.ListAPIView):
    serializer_class = ListPostTeamViewSerializers

    def get_queryset(self):
        return TeamPost.objects.\
            select_related('user', 'team_post').\
            prefetch_related('likes', 'dislikes').\
            filter(team_post_id=self.kwargs.get('pk'))


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

    def get_object(self):
        obj = TeamPost.objects.\
            select_related('user', 'team_post').\
            prefetch_related('likes', 'dislikes').\
            get(id=self.kwargs.get('num_post'))
        self.check_object_permissions(self.request, obj)
        return obj


class AddLikesOrDislikesTeamPostView(viewsets.ModelViewSet):
    queryset = TeamPost.objects.all()
    serializer_class = RetrievePostTeamSerializers
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = TeamPost.objects.\
            select_related('user__username', 'team_post__title').\
            prefetch_related('likes', 'dislikes').\
            get(id=self.kwargs.get('num_post'))
        self.check_object_permissions(self.request, obj)
        return obj

    @action(detail=True, methods=('put',))
    def set_like(self, request, pk, num_post):
        post = self.get_object()
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
        return CommentTeamPost.objects.select_related('user', 'comment_team_post').filter(comment_team_post_id=self.kwargs.get('num_post'))


class RetUpDesCommentsTeamPostView(MixedPermission, viewsets.ModelViewSet):
    queryset = CommentTeamPost.objects.select_related('user', 'comment_team_post').all()
    serializer_class = CommentsRetDesUpTeamPostSerializers
    permission_classes_by_action = {
        'retrieve': (IsAuthenticatedOrReadOnly,),
        'update': (IsUser,),
        'destroy': (IsUserInPostTeam, ),
    }
    lookup_url_kwarg = 'num_comment'


class CreateInviteTeamView(generics.CreateAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializers
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, team_id=self.kwargs.get('pk'))


class DelInviteTeamView(generics.DestroyAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializers
    permission_classes = (IsUser, )
    lookup_url_kwarg = 'num_invite'


class ListInviteTeamView(generics.ListAPIView):
    queryset = Invite.objects.select_related('user', 'team').all()
    serializer_class = ListInviteTeamSerializers
    permission_classes = (IsUserTeam, )


class RetrieveUpdateInviteTeamView(MixedSerializer, viewsets.ModelViewSet):
    queryset = Invite.objects.select_related('user', 'team').all()
    serializer_classes_by_action = {
        'retrieve': RetrieveInviteSerializers,
        'update': UpdateInviteSerializers,
    }
    permission_classes = (IsAdminTeam, )
    lookup_url_kwarg = 'num_invite'

    def perform_update(self, serializer):
        serializer.save()
        if serializer.data['permit']:
            self.save_invite()
            self.delete_invite()
        elif not(serializer.data['process']):
            self.delete_invite()

    def save_invite(self):
        user, team = self.get_object().user.id, self.get_object().team.id
        subs = SubscribersTeam()
        subs.user_id = user
        subs.team_id = team
        subs.save()

    def delete_invite(self):
        invite = self.get_object()
        invite.delete()

