from django.urls import path

from .views import (ListTeamView,
                    RetrieveTeamView,
                    ListPostTeamView,
                    RetrieveEditUserPostView,
                    CreateTeamView, AddPostTeamView,
                    AddDelFollowingTeamView,
                    TeamEditRetrieveUpdateDestroyView, AddLikesOrDislikesTeamPostView,
                    )

urlpatterns = [
    path('', ListTeamView.as_view()),
    path('create/', CreateTeamView.as_view()),
    path('<int:pk>/', RetrieveTeamView.as_view()),
    path('<int:pk>/add_del_following', AddDelFollowingTeamView.as_view({'put': 'add_del_following', })),
    path('<int:pk>/add_post', RetrieveTeamView.as_view()),
    path('<int:pk>/edit/', TeamEditRetrieveUpdateDestroyView.as_view({
        'get': 'retrieve',
        "put": 'update',
        'delete': 'destroy'})
         ),
    path('<int:pk>/wall/', ListPostTeamView.as_view()),
    path('<int:pk>/wall/add_post', AddPostTeamView.as_view({'post': 'create', })),
    path('<int:pk>/wall/<int:num_post>/', RetrieveEditUserPostView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'})
         ),
    path('<int:pk>/wall/<int:num_post>/add-like/', AddLikesOrDislikesTeamPostView.as_view({'put': 'set_like'})),
    path('<int:pk>/wall/<int:num_post>/add-dislike/', AddLikesOrDislikesTeamPostView.as_view({'put': 'set_dislike'})),

]
