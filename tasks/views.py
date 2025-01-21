from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView

from tasks.forms import CreateTaskForm
from tasks.models import Tasks


class CreateTaskView(CreateView):
    model = Tasks
    form_class = CreateTaskForm
    template_name = 'tasks/create-task.html'