from django.contrib import admin

from .models import Task
# Register your models here.

admin.site.register(Task)


# @admin.register(Task)
# class Taskmodeladmin(admin.ModelAdmin):
#     class Meta:
#         model = Task
#         fields = ('user', 'text', 'is_done', 'created')
