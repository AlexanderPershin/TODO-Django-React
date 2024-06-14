from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from tasks.api.views import TasksListView, TaskDetailAPIView, send_message_to_user

app_name = "tasks"

router = DefaultRouter()
router.register(r"task", TaskDetailAPIView)

urlpatterns = [
    path(
        "",
        include(router.urls),
        name="task_details",
    ),
    path("tasks/", TasksListView.as_view(), name="tasks_list"),
    path('sockets/msg-to-user/', send_message_to_user, name="send_msg_to_user")
]
