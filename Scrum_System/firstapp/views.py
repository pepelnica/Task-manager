from django.shortcuts import render, HttpResponseRedirect, HttpResponsePermanentRedirect, reverse, redirect
from django.http import HttpResponseNotFound, HttpResponse
from .forms import task_create_form, RegistrationForm, AuthForm, BoardCreate, task_edit_form
from .models import Task, Account, Boards
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required, permission_required

statuses = ["NOT_ACCEPTED", "ACCEPTED", "IN_PROGRESS", "COMPLETED"]


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password_0"])
            new_user.save()
            Account.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})

    else:
        form = RegistrationForm()
    return render(request, "account/registration.html", {"form": form})


@login_required
def main_page(request):
    return render(request, "account/main_page.html", {"section": main_page})


@login_required
def boards(request, id):
    board = Boards.objects.get(id=id)

    not_accepted_tasks = Task.objects.filter(task_status='NOT_ACCEPTED', task_parent = board)
    accepted_tasks = Task.objects.filter(task_status='ACCEPTED', task_parent = board)
    in_progress_tasks = Task.objects.filter(task_status='IN_PROGRESS', task_parent = board)
    completed_tasks = Task.objects.filter(task_status='COMPLETED', task_parent = board)
    task_create = task_create_form()
    return render(request, "board/board.html", {"not_accepted_tasks": not_accepted_tasks,
                                          "accepted_tasks": accepted_tasks,
                                          "in_progress_tasks": in_progress_tasks,
                                          "completed_tasks": completed_tasks,
                                          "form": task_create,
                                          "board": board})

@login_required
def create_board(request):
    if request.method == "POST":
        board = Boards() 
        board.name = request.POST.get("name")
        board.save()

        account = Account.objects.get(user=request.user)
        board.users.add(account)
        board.save()

        return render(request, "account/main_page.html")
    else:
        form = BoardCreate()
        return render(request, "board/create_board.html", {"form": form})


@login_required
def create_task(request, id):
    board = Boards.objects.get(id=id)
    if request.method == "POST":
        task_ = Task()
        task_.task_title = request.POST.get("title")
        task_.task_text = request.POST.get("text")
        task_.time_of_ending = request.POST.get("end_of_task")
        task_.task_status = request.POST.get("status")
        board.task_set.add(task_, bulk = False)
        task_.save()
        board.save()
        return redirect("/account/main_page/board/" + str(board.id))



def edit_task(request, id):
    task = Task.objects.get(id=id)
    id_ = task.task_parent.id
    if request.method == "POST":
        task = task_edit_form(request.POST, instance=task)
        task.save()
        return redirect("/account/main_page/board/" + str(id_))
    else:
        form = task_edit_form(instance=task)
        return render(request, "task_edit.html", {"task": task, "form": form})

 

def delete_task(request, id):
    task_ = Task.objects.get(id=id)
    id_ = task_.task_parent.id
    task_.delete()
    return redirect("/account/main_page/board/" + str(id_))


def status_change_up(request, id):
    if request.method == "POST":
        task_ = Task.objects.get(id=id)
        id_ = task_.task_parent.id
        old_status_id = statuses.index(task_.task_status)
        task_.task_status = statuses[old_status_id+1]
        task_.save()
    return redirect("/account/main_page/board/" + str(id_))


def status_change_down(request, id):
    if request.method == "POST":
        task_ = Task.objects.get(id=id)
        id_ = task_.task_parent.id
        old_status_id = statuses.index(task_.task_status)
        task_.task_status = statuses[old_status_id-1]
        task_.save()
    return redirect("/account/main_page/board/" + str(id_))


@login_required
def list_of_boards(request):
    boards = Boards.objects.filter(users__user = request.user)
    return render(request, "account/main_page.html", {"boards": boards})
 






