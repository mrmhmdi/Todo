from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='update'),
    path('create_task/', views.TaskCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete')
]
