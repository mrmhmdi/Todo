from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import SignUpForm

# Create your views here.


class SignUpCreateView(CreateView):
    form_class = SignUpForm
    redirect_authenticated_user = True
    template_name = "authentication/signup_page.html"
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            return redirect('main')
        return super().get(request, *args, **kwargs)


class LoginViewPage(LoginView):
    template_name = 'authentication/login_page.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')
