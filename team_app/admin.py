from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Team, TeamPost, Category, Stack, Invite, SubscribersTeam, CommentTeamPost


class TeamPostInlines(admin.StackedInline):
    model = TeamPost
    extra = 0


class SubscribersTeamAdminInline(admin.StackedInline):
    model = SubscribersTeam
    extra = 0


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'category', 'user', )
    list_display_links = ('title', )
    list_filter = ('category', 'stack', )
    search_fields = ('title', 'user', )
    readonly_fields = ('get_image', )
    inlines = (TeamPostInlines, SubscribersTeamAdminInline)

    def get_image(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src={obj.avatar.url} width="50" height="60"')
        return mark_safe(f'<img src='' width="50" height="60"')

    get_image.short_description = 'Аватарка'


@admin.register(TeamPost)
class TeamPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'team_post', 'user', 'get_image')
    list_display_links = ('title', )
    search_fields = ('user', 'team_post', 'title', )
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        if obj.poster:
            return mark_safe(f'<img src={obj.poster.url} width="50" height="60"')
        return mark_safe(f'<img src='' width="50" height="60"')

    get_image.short_description = 'Постер'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )


@admin.register(Invite)
class InviteAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'datetime_push_invite', )
    list_display_links = ('user', )


@admin.register(SubscribersTeam)
class SubscribersTeamAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'is_moder', )
    list_display_links = ('user', )


@admin.register(CommentTeamPost)
class CommentTeamPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment_team_post')

