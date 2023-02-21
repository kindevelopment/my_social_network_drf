from rest_framework import serializers

from .models import Subscribe, UserPost
from .serializers import UserSerializers


def get_all_post_subscribers(self, request):
    follows = Subscribe.objects.get(user=request.user).follow.values_list('id')
    all_post = UserPost.objects.filter(user_id__in=follows)
    return all_post


class AllPostSubscribeSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    likes = UserSerializers(many=True)
    dislikes = UserSerializers(many=True)

    class Meta:
        model = UserPost
        exclude = ('id', )