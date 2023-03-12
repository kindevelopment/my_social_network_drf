from django_filters import rest_framework as filters
from .models import SubscribersTeam, Team


def get_all_follow_team(request):
    return SubscribersTeam.objects.filter(user=request.user)


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ListTeamFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__title', lookup_expr='in')
    stack = CharFilterInFilter(field_name='stack__title', lookup_expr='in')

    class Meta:
        model = Team
        fields = ['category', 'stack']