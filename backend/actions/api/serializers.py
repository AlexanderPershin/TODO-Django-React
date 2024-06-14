from rest_framework.serializers import ModelSerializer
from actions.models import Action


class ActionSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop("many", True)
        super(ActionSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Action
        fields = "__all__"
