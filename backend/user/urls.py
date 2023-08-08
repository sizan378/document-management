from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from user.views.user_login import UserLoginView
from user.views.user_registration import UserRegistrationView
from user.views.user_list import AdminUsersListView

urlpatterns = [
    # http://localhost:8011/api/v1/user/registration/
    path(
        route="registration/",
        view=UserRegistrationView.as_view(),
        name="user_registration",
    ),

    # http://localhost:8011/api/v1/user/login/
    path(
        route="login/",
        view=UserLoginView.as_view(),
        name="user_login",
    ),

    # http://localhost:8011/api/v1/user/admin/refresh-token/
    path(
        route="admin/refresh-token/",
        view=jwt_views.TokenRefreshView.as_view(),
        name="token_refresh"
    ),

    # http://localhost:8011/api/v1/user/admin/all-users/
    path(
        route="admin/all-users/",
        view=AdminUsersListView.as_view(),
        name="all_users_list_by_admin"
    ),
]
