from rest_framework.permissions import IsAuthenticated

from team_app.models import Team, SubscribersTeam, Invite


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


class IsAdminTeam(IsAuthenticated):

    def has_permission(self, request, view):
        return Team.objects.filter(user=request.user, id=view.kwargs.get('pk')).exists() \
            or SubscribersTeam.objects.filter(user=request.user, team_id=view.kwargs.get('pk'), is_moder=True).exists()


class IsAuthorTeam(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return Team.objects.filter(user=request.user, id=view.kwargs.get('pk')).exists() \
            or SubscribersTeam.objects.filter(user=request.user, team_id=view.kwargs.get('pk'), is_moder=True).exists() \
            or obj.user == request.user


class IsInvite(IsAuthenticated):
    def has_permission(self, request, view):
        return not(Team.objects.filter(user=request.user, id=view.kwargs.get('pk')).exists() \
            or SubscribersTeam.objects.filter(user=request.user, team_id=view.kwargs.get('pk')).exists() \
            or Invite.objects.filter(user=request.user, team_id=view.kwargs.get('pk')).exists())


class IsUserMessage(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj.user_sender == request.user or obj.user_reciever == request.user


class IsUserInPostTeam(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user