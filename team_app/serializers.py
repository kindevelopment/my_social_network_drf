from rest_framework import serializers
from .models import Team, TeamPost, Category, Stack
from profile_app.serializers import UserSerializers


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', )


class TeamPostFieldViewSerializers(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('title', )


class StackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ('title', )


class MixinFieldTeam(serializers.ModelSerializer):
    category = CategorySerializers()
    stack = StackSerializers(many=True)
    subscribers = UserSerializers(many=True)


class ListTeamViewSerializers(MixinFieldTeam, serializers.ModelSerializer):
    '''Вывод списком всех команд'''
    class Meta:
        model = Team
        exclude = ('user', 'about', )


class TeamCreateSerializers(serializers.ModelSerializer):
    '''Создание команды'''
    class Meta:
        model = Team
        fields = ('title', 'about', 'avatar', 'category', 'stack', )


class RetrieveTeamViewSerializers(MixinFieldTeam, serializers.ModelSerializer):
    '''Вывод детально одной команды'''
    user = UserSerializers()

    class Meta:
        model = Team
        fields = '__all__'


class EditDestroyViewSerializers(serializers.ModelSerializer):
    '''Изменение данных команды'''
    category = CategorySerializers()
    stack = StackSerializers(many=True)

    class Meta:
        model = Team
        exclude = ('user', 'subscribers', )


class ListPostTeamViewSerializers(serializers.ModelSerializer):
    '''Посты команды'''
    likes = UserSerializers(many=True)
    dislikes = UserSerializers(many=True)
    team_post = TeamPostFieldViewSerializers()

    class Meta:
        model = TeamPost
        fields = ('title', 'text', 'poster', 'likes', 'dislikes', 'team_post', )


class AddPostTeamSerializers(serializers.ModelSerializer):

    class Meta:
        model = TeamPost
        fields = ('title', 'text', 'poster')


class RetrieveEditUserPostSerializers(serializers.ModelSerializer):
    '''Изменение и удаление поста команды'''
    user = UserSerializers()
    likes = UserSerializers(many=True)
    dislikes = UserSerializers(many=True)

    class Meta:
        model = TeamPost
        exclude = ('team_post', )


class RetrievePostTeamSerializers(serializers.ModelSerializer):
    '''Выведение детально одного поста'''
    class Meta:
        model = TeamPost
        fields = '__all__'