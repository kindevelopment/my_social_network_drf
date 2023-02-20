from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import User, UserPost, Subscribe, CommentUserPost
from .serializers import (ProfileSerializers,
                          ProfileEditSerializers,
                          UserPostListSerializers,
                          UserPostRetrieveAndEdit,
                          ListUserSerializers,
                          ProfileSubscribeSerializers,
                          UserPostAddSerializers,
                          CommentsCreateUserPostSerializers, CommentsListUserPostSerializers,
                          CommentsRetDesUpUserPostSerializers,
                          )

from base.classes import MixedPermission
from base.permissions import IsUser, IsUserprofile


class ListProfileView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListUserSerializers


class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializers


class ProfileSubscribeView(generics.RetrieveAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = ProfileSubscribeSerializers
    lookup_url_kwarg = 'pk'


class ProfileSubscribeAddDelView(viewsets.ModelViewSet):
    queryset = Subscribe.objects.all()
    serializer_class = ProfileSubscribeSerializers
    permission_classes = (IsAuthenticated, )

    @action(detail=True, methods=['put', ])
    def add_del_follower(self, request, pk):
        subscribe = self.get_object()
        user = Subscribe.objects.get(user_id=self.request.user.id)
        if self.request.user in subscribe.followers.all():
            subscribe.followers.remove(self.request.user)
            user.follow.remove(subscribe.user)
        else:
            subscribe.followers.add(self.request.user)
        return Response(status=201)


class ProfileEditView(MixedPermission, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileEditSerializers
    permission_classes_by_action = {
        'retrieve': (IsAuthenticatedOrReadOnly,),
        'update': (IsUserprofile,),
        'destroy': (IsUserprofile,),
    }


class ListUserPostView(generics.ListAPIView):
    serializer_class = UserPostListSerializers

    def get_queryset(self):
        return UserPost.objects.filter(user_id=self.kwargs.get('pk'))


class UserPostAddView(generics.CreateAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostAddSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RetrieveUserPostView(MixedPermission, viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserPostRetrieveAndEdit
    permission_classes_by_action = {
        'retrieve': (IsAuthenticatedOrReadOnly,),
        'update': (IsUser,),
        'destroy': (IsUser,),
    }
    lookup_url_kwarg = 'num_post'


class AddLikesOrDislikesUserPostView(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserPostRetrieveAndEdit
    permission_classes = (IsAuthenticated, )
    lookup_url_kwarg = 'num_post'

    @action(detail=True, methods=('put', ))
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


class AddCommentsUserPostView(generics.CreateAPIView):
    queryset = CommentUserPost.objects.all()
    serializer_class = CommentsCreateUserPostSerializers
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, comment_user_post_id=self.kwargs.get('num_post'))


class ListCommentsUserPostView(generics.ListAPIView):
    serializer_class = CommentsListUserPostSerializers

    def get_queryset(self):
        return CommentUserPost.objects.filter(comment_user_post_id=self.kwargs.get('num_post'))


class RetUpDesCommentsUserPostView(MixedPermission, viewsets.ModelViewSet):
    queryset = CommentUserPost.objects.all()
    serializer_class = CommentsRetDesUpUserPostSerializers
    permission_classes_by_action = {
        'retrieve': (IsAuthenticatedOrReadOnly,),
        'update': (IsUser,),
        'destroy': (IsUser,),
    }
    lookup_url_kwarg = 'num_post'