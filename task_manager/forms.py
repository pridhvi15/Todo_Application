from django import forms

from task_manager.models import User,TaskModel

class Userform(forms.ModelForm):

    class Meta:

        model = User

        fields = ["usname","first_name","last_name","email","password"]

        widgets = {
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the username:"}),
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the firstname:"}),
            "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the lastname:"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter the email:"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter the password"})
        }

class Login_form(forms.Form):

    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter username:"}))

    password = forms.CharField(max_length=120,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password:"}))

class Task_Form(forms.ModelForm):

    class Meta:

        model = TaskModel

        fields = ["task_name","task_description","due_date","priority"]

        widgets = {
            "task_name" : forms.TextInput(attrs={"class":"form-control","placeholder":"Enter the task name:"}),
            "task_description" : forms.Textarea(attrs={"class":"form-control","placeholder":"Enter the description:"}),
            "due_date" : forms.DateTimeInput(attrs={"class":"form-control","placeholder":"Enter the date","type":"date"}),
            "priority" : forms.Select(attrs={"class":"form-control","placeholder":"Enter the priority"})
        }





