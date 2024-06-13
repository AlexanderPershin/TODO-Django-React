from rest_framework.serializers import ModelSerializer
from tasks.models import Task


class TaskSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop("many", True)
        super(TaskSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Task
        fields = "__all__"
