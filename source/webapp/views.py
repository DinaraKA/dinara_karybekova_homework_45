from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, STATUS_CHOICES
from webapp.form import TaskForm


def index_view(request, *args, **kwargs):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks': tasks
    })


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })


def task_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                details=form.cleaned_data['details'],
                date=form.cleaned_data['date']
            )
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'task':task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(data={
            'description': task.description,
            'status': task.status,
            'details': task.details,
            'date': task.date
        })
        return render(request, 'edit.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            description = form.cleaned_data['description'],
            status = form.cleaned_data['status'],
            details = form.cleaned_data['details'],
            date = form.cleaned_data['date']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'edit.html', context={'form': form, 'task': task})


