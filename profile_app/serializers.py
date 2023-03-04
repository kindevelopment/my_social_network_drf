from rest_framework import serializers
from rest_framework.utils.serializer_helpers import BindingDict

from .models import (User,
                     UserPost,
                     Subscribe,
                     CommentUserPost,
                     )


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', )


class AllPostSubscribeSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    likes = UserSerializers(many=True)
    dislikes = UserSerializers(many=True)

    class Meta:
        model = UserPost
        exclude = ('id', )


class MixinFieldProfile(serializers.ModelSerializer):
    user = UserSerializers()
    likes = UserSerializers(many=True)
    dislikes = UserSerializers(many=True)


class ListUserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'avatar', 'username', 'address')


class ProfileSerializers(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {key: value for key, value in instance.items()}


class ProfileListSubscribeSerializers(serializers.ModelSerializer):
    subscribe = UserSerializers()

    class Meta:
        model = Subscribe
        fields = ('subscribe', 'id')


class ProfileSubscribeSerializers(serializers.ModelSerializer):
    subscribe = UserSerializers()
    user = UserSerializers()

    class Meta:
        model = Subscribe
        fields = '__all__'


class ProfileEditSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'about', 'avatar', 'address', 'phone_num', 'url_github', 'hide_fields', )


class UserPostListSerializers(MixinFieldProfile, serializers.ModelSerializer):

    class Meta:
        model = UserPost
        fields = ('id', 'user', 'title', 'text', 'poster', 'likes', 'dislikes', )


class UserPostAddSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserPost
        fields = ('title', 'text', 'poster', )


class UserPostRetrieveAndEdit(MixinFieldProfile, serializers.ModelSerializer):

    class Meta:
        model = UserPost
        fields = '__all__'


class CommentsCreateUserPostSerializers(serializers.ModelSerializer):

    class Meta:
        model = CommentUserPost
        fields = ('text', )


class CommentsListUserPostSerializers(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = CommentUserPost
        exclude = ('comment_user_post', )


class CommentsRetDesUpUserPostSerializers(serializers.ModelSerializer):

    class Meta:
        model = CommentUserPost
        fields = ('text', )