import logging
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# from rest_framework.decorators import (
#     api_view,
#     authentication_classes,
#     permission_classes,
# )
from tasks.models import Task
from tasks.api.serializers import TaskSerializer


logger = logging.getLogger(__name__)


class TasksListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Allows to filter using query parameters
        """
        search = self.request.query_params.get("search", None)

        queryset = Task.objects.all()
        queryset = queryset.filter(owner=self.request.user)

        if search:
            search_query = Q(title__icontains=search) | Q(body__icontains=search)
            queryset = queryset.filter(search_query)

        return queryset


class TaskDetailAPIView(viewsets.ModelViewSet):
    model = Task
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset

    def retrieve(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            data["owner"] = request.user.pk
            serializer = self.get_serializer(data=data, many=isinstance(data, list))
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        except Exception as error:
            logger.error(f"Task model validation error: {error}", exc_info=True)
            return Response(
                {"detail": "Task validation failed"},
                status=status.HTTP_400_BAD_REQUEST,
            )
