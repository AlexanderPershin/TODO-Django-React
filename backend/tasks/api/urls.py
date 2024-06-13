from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from tasks.api.views import TasksListView, TaskDetailAPIView

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
]
