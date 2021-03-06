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

urlpatterns = [
    path('', views.boards),
    path('boards/<int:id>', views.boards),
    path('create_task/', views.create_task),
    path('delete_task/<int:id>', views.delete_task),
    path('status_change_up/<int:id>', views.status_change_up),
    path('status_change_down/<int:id>', views.status_change_down),
    path('edit_task/<int:id>', views.edit_task),
    path('login/', views.authorization),
    path('admin/', admin.site.urls),
    path('registration/', views.registration),
]
