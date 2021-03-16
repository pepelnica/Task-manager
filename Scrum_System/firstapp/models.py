from django.db import models
from django.conf import settings


class Boards(models.Model):
    name = models.CharField(max_length=20)


class Task(models.Model):
    task_title = models.CharField(max_length=20)
    task_text = models.CharField(max_length=100)
    time_of_ending = models.DateField()
    task_status_choices = (
        ('NOT_ACCEPTED', 'Not accepted'),
        ('ACCEPTED', 'Accepted'),
        ('IN_PROGRESS', 'In progress'),
        ('COMPLETED', 'Completed'),
    )
    task_status = models.CharField(choices=task_status_choices, default='NOT_ACCEPTED', max_length=20)
    task_parent = models.ForeignKey(Boards, on_delete=models.CASCADE, default=1)
    #task_executors =


class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    boards = models.ManyToManyField(Boards)
# Create your models here.
