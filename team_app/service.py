from rest_framework import serializers

from .models import SubscribersTeam
from .serializers import TeamFieldSerializers


def get_all_follow_team(request):
    all_team = SubscribersTeam.objects.filter(user=request.user)
    return all_team


