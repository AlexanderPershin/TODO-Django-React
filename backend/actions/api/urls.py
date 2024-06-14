from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from actions.api.views import ActionListView, get_action

app_name = "actions"


urlpatterns = [
    path("actions/", ActionListView.as_view(), name="actions_list"),
    path("action/<str:action_id>/", get_action, name="get_action"),
]
