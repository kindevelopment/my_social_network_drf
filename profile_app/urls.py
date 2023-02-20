from django.urls import path
from .views import (ProfileView,
                    ProfileEditView,
                    ListUserPostView,
                    RetrieveUserPostView,
                    ListProfileView,
                    ProfileSubscribeView,
                    ProfileSubscribeAddDelView,
                    UserPostAddView,
                    AddLikesOrDislikesUserPostView,
                    AddCommentsUserPostView,
                    ListCommentsUserPostView,
                    )

urlpatterns = [
    path('', ListProfileView.as_view()),
    path('<int:pk>/', ProfileView.as_view()),
    path('<int:pk>/subscribe/', ProfileSubscribeView.as_view()),
    path('<int:pk>/subscribe/add_del/', ProfileSubscribeAddDelView.as_view({
        'get': 'retrieve',
        'put': 'add_del_follower'})
         ),
    path('<int:pk>/edit/', ProfileEditView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'})
         ),
    path('<int:pk>/wall/', ListUserPostView.as_view()),
    path('<int:pk>/wall/add_post', UserPostAddView.as_view()),
    path('<int:pk>/wall/<int:num_post>/', RetrieveUserPostView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'})
         ),
    path('<int:pk>/wall/<int:num_post>/add-like/', AddLikesOrDislikesUserPostView.as_view({'put': 'set_like'})),
    path('<int:pk>/wall/<int:num_post>/add-dislike/', AddLikesOrDislikesUserPostView.as_view({'put': 'set_dislike'})),
    path('<int:pk>/wall/<int:num_post>/comments/add', AddCommentsUserPostView.as_view()),
    path('<int:pk>/wall/<int:num_post>/comments/', ListCommentsUserPostView.as_view()),
]