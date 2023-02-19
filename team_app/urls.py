from django.urls import path

from .views import ListTeamView, RetrieveTeamView, ListPostTeamView, RetrieveEditUserPostView, TeamEditDestroyView

urlpatterns = [
    path('', ListTeamView.as_view()),
    path('<int:pk>/', RetrieveTeamView.as_view()),
    path('<int:pk>/edit/', TeamEditDestroyView.as_view({'get': 'retrieve', "put": 'update', 'delete': 'destroy'})),
    path('<int:pk>/wall/', ListPostTeamView.as_view()),
    path('<int:pk>/wall/<int:num_post>/', RetrieveEditUserPostView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'})
         ),
]
