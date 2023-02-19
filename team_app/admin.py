from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Team, TeamPost, Category, Stack, Invite


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'category', 'user', )
    list_display_links = ('title', )
    list_filter = ('category', 'stack', )
    search_fields = ('title', 'user', )
    readonly_fields = ('get_image', )


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="50" height="60"')

    get_image.short_description = 'Аватарка'


@admin.register(TeamPost)
class TeamPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'team_post', 'user', 'get_image')
    list_display_links = ('title', )
    search_fields = ('user', 'team_post', 'title', )
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="60"')

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