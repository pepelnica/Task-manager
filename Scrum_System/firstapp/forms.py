from django import forms
from django.contrib.auth.models import User
from .models import Profile

task_status_choices = (
        ('NOT_ACCEPTED', 'Not accepted'),
        ('ACCEPTED', 'Accepted'),
        ('IN_PROGRESS', 'In progress'),
        ('COMPLETED', 'Completed'),
)

class task_create_form(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea, max_length=100)
    status = forms.ChoiceField(choices=task_status_choices)
    #выпадающее окно с пользователями доски
    end_of_task = forms.DateField()

class user_create_form(forms.Form):
    password_1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password_1'] != cd['password_2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password_2']