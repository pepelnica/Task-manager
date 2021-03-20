"""Scrum_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from firstapp import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('main_page/', views.main_page, name='main_page'),
    path('main_page/board/<int:id>', views.boards, name="board"),
    path('main_page/board/create_task/<int:id>', views.create_task),
    path('main_page/board/delete_task/<int:id>', views.delete_task),
    path('main_page/board/status_change_up/<int:id>', views.status_change_up),
    path('main_page/board/status_change_down/<int:id>', views.status_change_down),
    path('main_page/board/edit_task/<int:id>', views.edit_task),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', views.registration, name="registration"),
    path('create_board/', views.create_board, name='create_board'),
    path('main_page/delete_board/<int:id>', views.delete_board, name='delete_board'),

]
