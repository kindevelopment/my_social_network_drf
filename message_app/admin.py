from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user_sender', 'user_reciever', 'time_send_message')
    list_display_links = ('user_sender', )
    search_fields = ('user_sender', 'user_reciever', )
    