from rest_framework.response import Response

from rest_framework.views import APIView

from profile_app.service import get_all_post_subscribers, AllPostSubscribeSerializers


class AllPostSubscribeView(APIView):

    def get(self, request):
        all_post = get_all_post_subscribers(self, request)
        print(all_post)
        serializer = AllPostSubscribeSerializers(all_post, many=True)
        return Response(serializer.data)