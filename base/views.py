from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import Task
# Create your views here.


class MainView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "base/main.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user=self.request.user)
        context['undone_count'] = context['tasks'].filter(
            is_done=False).count()

        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['tasks'] = Task.objects.filter(
                text__icontains=search_input, user=self.request.user)
        context['search_input'] = search_input
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['text']
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['text', 'is_done']
    success_url = reverse_lazy('main')

    def get_queryset(self):
        return self.request.user.task_set


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('main')

    def get_queryset(self):
        return self.request.user.task_set
