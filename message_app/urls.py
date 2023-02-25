from django.urls import path

from .views import MessageListView, MessageRetrieveView

urlpatterns = [
    path('', MessageListView.as_view()),
    path('<int:pk>/', MessageRetrieveView.as_view({'get': 'retrieve', 'delete': 'destroy'})),

]