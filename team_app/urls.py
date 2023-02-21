from django.urls import path

from .views import (ListTeamView,
                    RetrieveTeamView,
                    ListPostTeamView,
                    RetrieveEditUserPostView,
                    CreateTeamView, AddPostTeamView,
                    DelFollowingTeamView,
                    TeamEditRetrieveUpdateDestroyView,
                    AddLikesOrDislikesTeamPostView,
                    AddCommentsTeamPostView,
                    ListCommentsTeamPostView,
                    RetUpDesCommentsTeamPostView,
                    CreateInviteTeamView,
                    ListSubscribersView,
    # DelInviteTeamView,
                    )

urlpatterns = [
    path('', ListTeamView.as_view()),
    path('create/', CreateTeamView.as_view()),
    path('<int:pk>/', RetrieveTeamView.as_view()),
    path('<int:pk>/list-subscribers', ListSubscribersView.as_view()),
    path('<int:pk>/del-subscriber/<int:num_user_fol>/', DelFollowingTeamView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'})),
    path('<int:pk>/edit/', TeamEditRetrieveUpdateDestroyView.as_view({
        'get': 'retrieve',
        "put": 'update',
        'delete': 'destroy'})
         ),
    path('<int:pk>/wall/', ListPostTeamView.as_view()),
    path('<int:pk>/wall/add-post', AddPostTeamView.as_view({'post': 'create', })),
    path('<int:pk>/wall/<int:num_post>/', RetrieveEditUserPostView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'})
         ),
    path('<int:pk>/wall/<int:num_post>/add-like/', AddLikesOrDislikesTeamPostView.as_view({'put': 'set_like'})),
    path('<int:pk>/wall/<int:num_post>/add-dislike/', AddLikesOrDislikesTeamPostView.as_view({'put': 'set_dislike'})),
    path('<int:pk>/wall/<int:num_post>/comments/', ListCommentsTeamPostView.as_view()),
    path('<int:pk>/wall/<int:num_post>/comments/add', AddCommentsTeamPostView.as_view({'post': 'create', })),
    path('<int:pk>/wall/<int:num_post>/comments/<int:num_comment>/', RetUpDesCommentsTeamPostView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'})
         ),
    path('<int:pk>/add-invite', CreateInviteTeamView.as_view()),
    # path('<int:pk>/del-invite/<int:num_invite>', DelInviteTeamView.as_view()),

]
