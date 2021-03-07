from django.shortcuts import render, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponseNotFound
from .forms import task_create_form, user_create_form
from .models import Task

statuses = ["NOT_ACCEPTED", "ACCEPTED", "IN_PROGRESS", "COMPLETED"]

def create_user(request):
    #if request.method == "POST":
    user_create = user_create_form()
    return render(request, "login.html", {"form": user_create})


def boards(request):
    not_accepted_tasks = Task.objects.filter(task_status='NOT_ACCEPTED')
    accepted_tasks = Task.objects.filter(task_status='ACCEPTED')
    in_progress_tasks = Task.objects.filter(task_status='IN_PROGRESS')
    completed_tasks = Task.objects.filter(task_status='COMPLETED')
    task_create = task_create_form()
    return render(request, "index.html", {"not_accepted_tasks": not_accepted_tasks,
                                          "accepted_tasks": accepted_tasks,
                                          "in_progress_tasks": in_progress_tasks,
                                          "completed_tasks": completed_tasks,
                                          "form": task_create})

def create_task(request):
    if request.method == "POST":
        task_ = Task()
        task_.task_title = request.POST.get("title")
        task_.task_text = request.POST.get("text")
        task_.time_of_ending = request.POST.get("end_of_task")
        task_.task_status = request.POST.get("status")
        task_.save()
    return HttpResponseRedirect("/")

def edit_task(request, id):
    try:
        task_create = task_create_form()
        task_ = Task.objects.get(id=id)
        task_create.text = task_.task_text
        task_create.title = task_.task_title
        if request.method == "POST":
            task_.task_title = request.POST.get("title")
            task_.task_text = request.POST.get("text")
            task_.time_of_ending = request.POST.get("end_of_task")
            task_.task_status = request.POST.get("status")
            task_.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "task_edit.html", {"task": task_, "form": task_create})
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Task not found</h2>")

def delete_task(request, id):
    task_ = Task.objects.get(id=id)
    task_.delete()
    return HttpResponseRedirect("/")

def status_change_up(request, id):
    if request.method == "POST":
        task_ = Task.objects.get(id=id)
        old_status_id = statuses.index(task_.task_status)
        task_.task_status = statuses[old_status_id+1]
        task_.save()
    return HttpResponseRedirect("/")

def status_change_down(request, id):
    if request.method == "POST":
        task_ = Task.objects.get(id=id)
        old_status_id = statuses.index(task_.task_status)
        task_.task_status = statuses[old_status_id-1]
        task_.save()
    return HttpResponseRedirect("/")
