from .models import UserPost


def get_all_post_subscribers(request):
    return UserPost.objects.filter(user__subscribe_in_user__user=request.user).order_by('-publish_time')

