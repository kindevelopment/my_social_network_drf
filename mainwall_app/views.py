from rest_framework.response import Response

from rest_framework.views import APIView

from profile_app.service import get_all_post_subscribers
from profile_app.serializers import AllPostSubscribeSerializers

from team_app.service import get_all_follow_team
from team_app.serializers import AllFollowTeamSerializers


class AllPostSubscribeView(APIView):

    def get(self, request):
        all_post = get_all_post_subscribers(request)
        serializer = AllPostSubscribeSerializers(all_post, many=True)
        return Response(serializer.data)


class AllFollowTeamView(APIView):

    def get(self, request):
        all_post = get_all_follow_team(request)
        serializer = AllFollowTeamSerializers(all_post, many=True)
        return Response(serializer.data)