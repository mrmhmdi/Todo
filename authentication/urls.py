from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('signup/', views.SignUpCreateView.as_view(), name='signup'),
    path('login/', views.LoginViewPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]
