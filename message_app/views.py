from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Message
from .serializers import (MessageListSerializers,
                          MessageRetrieveSerializers,
                          MessageCreateSerializers,
                          )

from base.permissions import IsUserMessage

from profile_app.models import User

from profile_app.serializers import UserSerializers


#  Мне нужно вывести всех уникальных пользователей которым я писал, либо которые писали мне
class MessageListView(generics.ListAPIView):
    serializer_class = UserSerializers
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user_sender = Message.objects.filter(user_sender=self.request.user).values_list('user_reciever')
        user_reciever = Message.objects.filter(user_reciever=self.request.user).values_list('user_sender')
        mymessage = user_sender.union(user_reciever)
        return User.objects.filter(id__in=mymessage)


class RoomMessage(generics.ListAPIView):
    serializer_class = MessageListSerializers
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Message.objects.filter(Q(user_sender=self.request.user) | Q(user_reciever=self.request.user), Q(user_sender=self.kwargs.get('pk')) | Q(user_reciever=self.kwargs.get('pk')), ~Q(hide__contains=self.request.user.id))


class MessageRetrieveView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageRetrieveSerializers
    permission_classes = (IsUserMessage, )
    lookup_url_kwarg = 'pk'

    def perform_destroy(self, instance):
        if self.request.user.id in instance.hide:
            pass
        else:
            instance.hide.append(self.request.user.id)
            instance.save()
            if len(instance.hide) > 1:
                instance.delete()


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializers
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user_sender=self.request.user, user_reciever_id=self.kwargs.get('pk'))