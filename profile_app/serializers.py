from rest_framework import serializers
from .models import User, UserPost, Subscribe


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', )


class MixinFieldProfile(serializers.ModelSerializer):
    user = UserSerializers()
    likes = UserSerializers(many=True)
    dislikes = UserSerializers(many=True)


class ListUserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'avatar', 'username', 'address')


class ProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('avatar', 'username', 'first_name', 'last_name', 'email', 'about', 'address', 'phone_num', 'url_github',)


class ProfileSubscribeSerializers(serializers.ModelSerializer):
    followers = UserSerializers(many=True)
    follow = UserSerializers(many=True)
    user = UserSerializers()

    class Meta:
        model = Subscribe
        fields = ('followers', 'follow', 'user', )


class ProfileEditSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'about', 'avatar', 'address', 'phone_num', 'url_github', )


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