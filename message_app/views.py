from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Message
from .serializers import MessageListSerializers, MessageRetrieveSerializers

from base.permissions import IsUserMessage


class MessageListView(generics.ListAPIView):
    serializer_class = MessageListSerializers
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Message.objects.filter(Q(user_sender=self.request.user) | Q(user_reciever=self.request.user), ~Q(hide__contains=self.request.user.id))


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
