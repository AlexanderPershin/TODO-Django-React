from django.urls import path
from users.api.views import UsersListView, UserRegistrationAPIView, get_current_user

app_name = "users"

urlpatterns = [
    path("users/", UsersListView.as_view(), name="users_list"),
    path("users/register/", UserRegistrationAPIView.as_view(), name="users_register"),
    path("users/current/", get_current_user, name="users_current"),
]
