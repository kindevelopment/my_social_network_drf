from django.urls import path

from .views import AllPostSubscribeView, AllFollowTeamView

urlpatterns = [
    path('', AllPostSubscribeView.as_view()),
    path('follow-team/', AllFollowTeamView.as_view()),

]