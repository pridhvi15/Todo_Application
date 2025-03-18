"""
URL configuration for ToDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from task_manager.views import Home,Userregister,Account_login,TaskAddView,TaskReadView,TaskDeleteView,TaskDetailsView,TaskUpdateView,Signout,Task_complete,User_Details_View,Reset_Password,WelcomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name="home"),
    path('task_manager/signup/',Userregister.as_view()),
    path('task_manager/login/',Account_login.as_view(),name="signin"),
    path('task_manager/welcome/',WelcomeView.as_view(),name="Welcome"),
    path('task_manager/taskadd/',TaskAddView.as_view(),name="task_add"),
    path('task_manager/alltask/',TaskReadView.as_view(),name="all_task"),
    path('task_manager/delete/<int:pk>',TaskDeleteView.as_view(),name="delete"),
    path('task_manager/details/<int:pk>',TaskDetailsView.as_view(),name='details'),
    path('task_manager/update/<int:pk>',TaskUpdateView.as_view()),
    path('task_manager/complete/<int:pk>',Task_complete.as_view(),name="complete"),
    path('task_manager/logout/',Signout.as_view()),
    path('task_manager/complete/',User_Details_View.as_view()),
    path('task_manager/reset/',Reset_Password.as_view(),name="reset")
]
