from django.urls import path

from .views import MessageListView, MessageRetrieveView, RoomMessage, MessageCreateView

urlpatterns = [
    path('', MessageListView.as_view()),
    path('chat/<int:pk>/', RoomMessage.as_view()),
    path('mes/create/<int:pk>/', MessageCreateView.as_view()),
    path('mes/<int:pk>/', MessageRetrieveView.as_view(
        {'get': 'retrieve', 'delete': 'destroy'}
    )),
]