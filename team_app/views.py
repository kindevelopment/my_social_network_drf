from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Team, TeamPost
from .serializers import ListTeamViewSerializers, RetrieveTeamViewSerializers, ListPostTeamViewSerializers, \
    RetrieveEditUserPostSerializers, EditDestroyViewSerializers
from base.classes import MixedPermission

from base.permissions import IsUser


class ListTeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = ListTeamViewSerializers


class RetrieveTeamView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = RetrieveTeamViewSerializers


class TeamEditDestroyView(MixedPermission, viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = EditDestroyViewSerializers
    permission_classes_by_action = {
        'retrieve': (IsAuthenticatedOrReadOnly,),
        'update': (IsUser,),
        'destroy': (IsUser,),
    }


class ListPostTeamView(generics.ListAPIView):
    serializer_class = ListPostTeamViewSerializers

    def get_queryset(self):
        return TeamPost.objects.filter(team_post_id=self.kwargs.get('pk'))


class RetrieveEditUserPostView(MixedPermission, viewsets.ModelViewSet):
    queryset = TeamPost.objects.all()
    serializer_class = RetrieveEditUserPostSerializers
    permission_classes_by_action = {
        'retrieve': (IsAuthenticatedOrReadOnly,),
        'update': (IsUser,),
        'destroy': (IsUser,),
    }
    lookup_url_kwarg = 'num_post'

