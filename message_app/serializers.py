from rest_framework import serializers

from .models import Message
from profile_app.serializers import UserSerializers


class MessageListSerializers(serializers.ModelSerializer):
    user_sender = UserSerializers()
    user_reciever = UserSerializers()

    class Meta:
        model = Message
        exclude = ('text_message', 'hide')


class MessageRetrieveSerializers(serializers.ModelSerializer):
    user_sender = UserSerializers()
    user_reciever = UserSerializers()

    class Meta:
        model = Message
        exclude = ('hide', )


class MessageCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('text_message', )