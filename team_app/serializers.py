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

    class Meta:
        model = Team
        exclude = ('user', 'about', )


class RetrieveTeamViewSerializers(MixinFieldTeam, serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Team
        fields = '__all__'


class EditDestroyViewSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    stack = StackSerializers(many=True)

    class Meta:
        model = Team
        exclude = ('user', 'subscribers', )


class ListPostTeamViewSerializers(serializers.ModelSerializer):
    likes = UserSerializers(many=True)
    dislikes = UserSerializers(many=True)
    team_post = TeamPostFieldViewSerializers()

    class Meta:
        model = TeamPost
        fields = ('title', 'text', 'poster', 'likes', 'dislikes', 'team_post', )


class RetrieveEditUserPostSerializers(serializers.ModelSerializer):

    class Meta:
        model = TeamPost
        exclude = ('team_post', )