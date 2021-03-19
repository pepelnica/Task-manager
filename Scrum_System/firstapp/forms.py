from django import forms
from django.contrib.auth.models import User
from .models import Boards, Task

task_status_choices = (
        ('NOT_ACCEPTED', 'Not accepted'),
        ('ACCEPTED', 'Accepted'),
        ('IN_PROGRESS', 'In progress'),
        ('COMPLETED', 'Completed'),
)


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class BoardCreate(forms.ModelForm):
    class Meta:
        model = Boards
        fields = ('name',)


class task_create_form(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea, max_length=100)
    status = forms.ChoiceField(choices=task_status_choices)
    #выпадающее окно с пользователями доски
    end_of_task = forms.DateField()

class task_edit_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_title', 'task_text', 'time_of_ending',)


class RegistrationForm(forms.ModelForm):
    password_0 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_1 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password_0'] != cd['password_1']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password_1']