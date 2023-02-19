from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import User, UserPost, Subscribe
from .serializers import (ProfileSerializers,
                          ProfileEditSerializers,
                          UserPostListSerializers,
                          UserPostRetrieveAndEdit,
                          ListUserSerializers,
                          ProfileSubscribeSerializers, UserPostAddSerializers,
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


