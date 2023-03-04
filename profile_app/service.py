from rest_framework import serializers

from .models import Subscribe, UserPost
from .serializers import UserSerializers


def get_all_post_subscribers(request):
    # try:
    #     follows = Subscribe.objects.get(user=request.user).follow.values_list('id')
    #     all_post = UserPost.objects.filter(user_id__in=follows)
    # except Subscribe.DoesNotExist:
    #     all_post = None
    # all_post = UserPost.objects.filter(user__user_follow_following__followers=request.user)
    all_post = UserPost.objects.filter(user__subscribe_in_user__user=request.user).order_by('-publish_time')
    return all_post

