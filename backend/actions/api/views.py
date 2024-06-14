import logging
import json
import socketio
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
import socketio.exceptions
from actions.models import Action
from actions.api.serializers import ActionSerializer

from sockets.sockets_client import sio


logger = logging.getLogger(__name__)


class ActionListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

    def get_queryset(self):
        queryset = Action.objects.filter(user=self.request.user)
        return queryset


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_action(request: Request, action_id: str):
    action = Action.objects.get(user=request.user, id=action_id)
    serializer = ActionSerializer(action)
    return Response(serializer.data)
