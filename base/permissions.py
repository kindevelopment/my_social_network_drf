from rest_framework.permissions import IsAuthenticated

from team_app.models import Team, SubscribersTeam


class IsUser(IsAuthenticated):
    """ Is Author of obj where only user """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsUserprofile(IsAuthenticated):
    """ Is Author of obj where only user """

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsUserInPost(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.comment_user_post.user.id or obj.user == request.user


class IsUserTeam(IsAuthenticated):

    def has_permission(self, request, view):
        return Team.objects.filter(user=request.user, id=view.kwargs.get('pk')).exists() \
            or SubscribersTeam.objects.filter(user=request.user, team_id=view.kwargs.get('pk')).exists()


class IsAuthorTeam(IsAuthenticated):

    def has_permission(self, request, view):
        return Team.objects.filter(user=request.user, id=view.kwargs.get('pk')).exists() \
            or SubscribersTeam.objects.filter(user=request.user, team_id=view.kwargs.get('pk'), is_moder=True).exists()


class IsAuthorObjTeam(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
