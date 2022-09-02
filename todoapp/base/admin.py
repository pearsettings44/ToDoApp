from django.contrib import admin
from .models import Task

# Register your models here.

# Add Task model to admin site
admin.site.register(Task)
