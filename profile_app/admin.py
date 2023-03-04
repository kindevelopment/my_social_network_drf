from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User, UserPost, CommentUserPost, Subscribe


class SubscribeAdminInline(admin.StackedInline):
    model = Subscribe
    extra = 0
    fk_name = 'user'


@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'get_image', )
    list_display_links = ('username', 'email', )
    search_fields = ('username', 'email', 'phone_num')
    readonly_fields = ('get_image', )
    inlines = (SubscribeAdminInline, )

    def get_image(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src={obj.avatar.url} width="50" height="60"')
        return mark_safe(f'<img src='' width="50" height="60"')

    get_image.short_description = 'Аватарка'


@admin.register(UserPost)
class UserPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'get_image', )
    list_display_links = ('title', )
    search_fields = ('title', 'user', )
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        if obj.poster:
            return mark_safe(f'<img src={obj.poster.url} width="50" height="60"')
        return mark_safe(f'<img src='' width="50" height="60"')

    get_image.short_description = 'Постер'


@admin.register(CommentUserPost)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment_user_post', )
    list_display_links = ('user', )
    search_fields = ('user', )


admin.site.register(Subscribe)