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
                    RetUpDesCommentsUserPostView,
                    DeleteSubsInUser,
                    )

urlpatterns = [
    path('', ListProfileView.as_view()),
    path('<int:pk>/', ProfileView.as_view()),
    path('<int:pk>/subscribe/', ProfileSubscribeView.as_view()),
    path('<int:pk>/subscribe/add-del/', ProfileSubscribeAddDelView.as_view({
        'get': 'retrieve',
        'put': 'add_del_follower', })
    ),
    path('<int:pk>/subscribe/del-subs/<int:num_subs>/', DeleteSubsInUser.as_view({
        'get': 'retrieve',
        'delete': 'destroy', })
    ),
    path('<int:pk>/edit/', ProfileEditView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'})
         ),
    path('<int:pk>/wall/', ListUserPostView.as_view()),
    path('<int:pk>/wall/add-post', UserPostAddView.as_view()),
    path('<int:pk>/wall/<int:num_post>/', RetrieveUserPostView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'})
         ),
    path('<int:pk>/wall/<int:num_post>/add-like/', AddLikesOrDislikesUserPostView.as_view({'put': 'set_like'})),
    path('<int:pk>/wall/<int:num_post>/add-dislike/', AddLikesOrDislikesUserPostView.as_view({'put': 'set_dislike'})),
    path('<int:pk>/wall/<int:num_post>/comments/', ListCommentsUserPostView.as_view()),
    path('<int:pk>/wall/<int:num_post>/comments/add', AddCommentsUserPostView.as_view()),
    path('<int:pk>/wall/<int:num_post>/comments/<int:num_comment>/', RetUpDesCommentsUserPostView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'})
         ),
]
