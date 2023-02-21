from django.urls import path

from .views import AllPostSubscribeView

urlpatterns = [
    path('', AllPostSubscribeView.as_view()),

]