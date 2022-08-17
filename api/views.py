from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from .serializer import Taskserializer
from base.models import Task
# Create your views here.


class TaskViewSet(ModelViewSet):
    serializer_class = Taskserializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.task_set.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        print(self.get_object().user)
        if self.request.user == self.get_object().user:
            return super().perform_destroy(instance)
        else:
            return Response('not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
