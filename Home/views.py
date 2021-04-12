from django.shortcuts import render , redirect
from Home.models import Tasks
from django.http import HttpResponse
from .form import *


def home(request):
    task_list = Tasks.objects.all()
    Add_task = aply_task()

    if request.method == 'POST':
        Add_task = aply_task(request.POST)
        if Add_task.is_valid():
            Add_task.save()
        return redirect('/')

    my_dict = {'Todo_list': task_list, 'form': Add_task}
    return render(request, 'Home/index.html', context=my_dict)


def update(request, pk):
    task = Tasks.objects.get(id=pk)
    form = update_form(instance=task)

    context = {'form': form}
    if request.method == 'POST':
        form = update_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'Update Template.html', context)


def delete_task(request, pk):
    item = Tasks.objects.get(id=pk)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'Delete.html', context)
