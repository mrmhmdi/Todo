from django.urls import include, path
from rest_framework import routers
from .views import TaskViewSet

router = routers.SimpleRouter()
router.register(r'', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
