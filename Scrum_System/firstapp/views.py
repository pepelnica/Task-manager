from django.shortcuts import render, HttpResponseRedirect, HttpResponsePermanentRedirect, reverse
from django.http import HttpResponseNotFound, HttpResponse
from .forms import task_create_form, RegistrationForm, AuthForm, BoardCreate
from .models import Task,  Account, Boards
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

statuses = ["NOT_ACCEPTED", "ACCEPTED", "IN_PROGRESS", "COMPLETED"]


def authorization(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/main_page/")
            else:
                return HttpResponse("Такого пользователя не существует")
        else:
            return HttpResponse("Неверный логин или пароль")
    else:
        form = AuthForm()
    return render(request, "login.html", {"form": form})


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_account = Account()
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password_0"])
            new_user.save()
            new_account.user.add(new_user)
            new_account.save()
            return HttpResponseRedirect("/main_page", )
    else:
        form = RegistrationForm()
    return render(request, "registration.html", {"form": form})


#def create_board(request):
 #   if request.method == "POST":
  #      board = BoardCreate(request.POST)
   #     board.save()
    #    return render(request, 'main_page.html')
    #else:
     #   _user = request.user
      #  form = BoardCreate()
       # print(_user.username)
        #return render(request, "main_page.html", {"form": form, "user": _user.username})


def main_page(request):
    user = request.user
    _form = BoardCreate()
    return render(request, "main_page.html", {"user": user, "form": _form})


def create_board(request):
    if request.method == "POST":
        board = Boards.objects.create(name=request.POST.get("name"))
        board.save()
        _user = request.user
        user_father = Account.objects.get(id=_user.id)
        user_father.boards.add(board)
        #_user.boards.create(name=request.POST.get("name"))
    return HttpResponseRedirect("/main_page")


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
