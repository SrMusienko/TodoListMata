from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


def mark(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()

    return redirect('task-list')


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo/task_list.html"
    paginate_by = 3
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task-list")
    template_name = "todo/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task-list")
    template_name = "todo/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")
    template_name = "todo/task_confirm_delete.html"


# --------------------Tag-------------------

class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo/tag_list.html"
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tag-list")
    template_name = "todo/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tag-list")
    template_name = "todo/task_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tag-list")
    template_name = "todo/tag_confirm_delete.html"
