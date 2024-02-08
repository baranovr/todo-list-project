from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TaskForm
from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo_list/task_list.html"

    def get_queryset(self):
        return Task.objects.all().order_by("-is_done", "-datetime")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:task-list")
    template_name = "todo_list/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task-list")
    template_name = "todo_list/task_form.html"


class TaskCompletedUpdateView(generic.UpdateView):
    model = Task
    fields = ("is_done", )
    success_url = reverse_lazy("todo_list:task-list")
    template_name = "todo_list/task_make_completed.html"


class TaskUndoUpdateView(generic.UpdateView):
    model = Task
    fields = ("is_done",)
    success_url = reverse_lazy("todo_list:task-list")
    template_name = "todo_list/task_undo.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:topic-list")
    template_name = "todo_list/task_confirm_delete.html"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo_list/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")
    template_name = "todo_list/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")
    template_name = "todo_list/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")
    template_name = "todo_list/tag_confirm_delete.html"
