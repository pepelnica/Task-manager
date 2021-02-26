from django.shortcuts import render, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import task_create_form, user_create_form
from .models import Task

def create_user(request):
    #if request.method == "POST":
    user_create = user_create_form()
    return render(request, "login.html", {"form": user_create})


def boards(request):
    tasks = Task.objects.all()
    not_accepted_tasks = Task.objects.filter(task_status='NOT_ACCEPTED')
    accepted_tasks = Task.objects.filter(task_status='ACCEPTED')
    in_progress_tasks = Task.objects.filter(task_status='IN_PROGRESS')
    completed_tasks = Task.objects.filter(task_status='COMPLETED')
    task_create = task_create_form()
    return render(request, "index.html", {"not_accepted_tasks": not_accepted_tasks,
                                          "accepted_tasks": accepted_tasks,
                                          "in_progress_tasks": in_progress_tasks,
                                          "completed_tasks": completed_tasks,
                                          "form": task_create,})

def create_task(request):
    if request.method == "POST":
        task_ = Task()
        task_.task_title = request.POST.get("title")
        task_.task_text = request.POST.get("text")
        task_.time_of_ending = request.POST.get("end_of_task")
        task_.task_status = request.POST.get("status")
        task_.save()
    return HttpResponseRedirect("/")

def delete_task(request, id):
    task_ = Task.objects.get(id=id)
    task_.delete()
    return HttpResponseRedirect("/")
