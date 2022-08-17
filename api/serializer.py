from rest_framework import serializers
from base.models import Task


class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'text', 'is_done', 'created',)
