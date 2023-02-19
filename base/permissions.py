from rest_framework.permissions import IsAuthenticated


class IsUser(IsAuthenticated):
    """ Is Author of obj where only user """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsUserprofile(IsAuthenticated):
    """ Is Author of obj where only user """

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsUserTeam(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        print(bool(request.user in obj.team_post.subscribers.all()))
        return request.user in obj.team_post.subscribers.all()
