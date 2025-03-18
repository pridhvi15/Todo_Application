from django.shortcuts import render,redirect
from django.views.generic import View
from task_manager.forms import Userform,Login_form,Task_Form,ForgetForm
from task_manager.models import User,TaskModel
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password

def is_user(fn):

    def wrapper(request,**kwargs):

        id = kwargs.get("pk")

        data = TaskModel.objects.get(id = id)

        if data.user == request.user:

            return fn(request,**kwargs)
        
        else:

            return redirect("signin")
        
    return wrapper

def is_login(fn):

    def wrapper(request,**kwargs):

        if not request.user.is_authenticated:

            return redirect("signin")
        
        else:

            return fn(request,**kwargs)
        
    return wrapper



# view = userregister
# method = get.post
# url = localhost:8000/task_manager/signup/

# Create your views here.

class Home(View):

    def get(self,request):

        return render(request,"home.html")

class Userregister(View):

    def get(self,request):

        form = Userform

        return render(request,"signup.html",{"form":form})
    
    def post(self,request):

        form = Userform

        data = Userform(request.POST)

        if data.is_valid():

            print(data.cleaned_data)

            User.objects.create_user(**data.cleaned_data)

        return render(request,"signup.html",{"form":form})
    
# url = lh:8000/task_manager/login/
# method = get,post
# view = Account_login
    
class Account_login(View):

    def get(self,request):

        form = Login_form

        return render(request,"Login.html",{"form":form})        
    
    def post(self,request):

        form = Login_form(request.POST)

        # data = Login_form(request.POST) # to get empty fields after else condition in the form

        # print(data)

        u_name = request.POST.get("username")

        pwd = request.POST.get("password")

        user_obj = authenticate(request,username = u_name,password = pwd)
        # print("tear up=====")

        if user_obj:

            # print("tear down=====")

            login(request,user_obj)

            return redirect("Welcome")
        
        else:

            return render(request,"login.html",{'form':form})
        
class WelcomeView(View):

    def get(self,request):

        data = TaskModel.objects.filter(user = request.user,status = False).values('id','task_name','task_description')

        return render(request,"welcome.html",{'data':data})

@method_decorator (decorator=is_login,name="dispatch")       
class TaskAddView(View):

    def get(self,request):

        form = Task_Form

        return render(request,"taskadd.html",{"form":form})
    
    def post(self,request):

        form = Task_Form(request.POST)

        if form.is_valid():

            TaskModel.objects.create(**form.cleaned_data,user=request.user)

        form = Task_Form

        return redirect("all_task")
    
# View = Read 
# url = lh:8000/task_manager/all_task/
# get

class TaskReadView(View):

    def get(self,request):

        data = TaskModel.objects.filter(user=request.user).order_by("status").values('id','task_name','task_description','status')

        return render(request,"alltask.html",{'data':data})


@ method_decorator ([is_user,is_login],name="dispatch")
class TaskDeleteView(View):

    def get(self,request,**kwargs):

        id = kwargs.get("pk")

        data=TaskModel.objects.get(id=id)

        data.delete()
        
        return redirect("all_task")

@ method_decorator(decorator=is_user,name="dispatch")
class TaskDetailsView(View):

    def get(self,request,**kwargs):

        id  = kwargs.get("pk")

        data = TaskModel.objects.get(id = id)

        return render(request,"details.html",{'data':data})
    
# url : lh:8000/task_manager/update/<int:pk>
# get post

@ method_decorator([is_user,is_login],name="dispatch")
class TaskUpdateView(View):

    def get(self,request,**kwargs):

        id  = kwargs.get("pk")

        data = TaskModel.objects.get(id = id)

        form = Task_Form(instance=data)

        return render(request,"update.html",{"form":form})
    
    def post(self,request,**kwargs):

        id = kwargs.get("pk")

        data = TaskModel.objects.get(id = id)

        form  = Task_Form(request.POST,instance=data)

        if form.is_valid():

            print("Done")

            form.save()

        return redirect("all_task")
    
class Task_complete(View):

    def get(seff,request,**kwargs):

        id = kwargs.get("pk")

        data = TaskModel.objects.get(id = id)

        data = data.complete()

        # if data.status == False:

        #     data.status = True

        #     data.save()
        next_url = request.GET.get("next") or "Welcome"

        return redirect(next_url)
    
class Signout(View):

    def get(self,request):

        logout(request)
        
        return redirect("home")

class User_Details_View(View):

    def get(self,request):

        total = TaskModel.objects.filter(user = request.user).count()

        # print(total)

        completed = TaskModel.objects.filter(user = request.user,status = True).count()

        incompleted = total-completed

        data = TaskModel.objects.filter(user = request.user)

        sum = 0

        for i in data:

            sum +=i.point

        print(sum)

        return render(request,"welcome.html",{"total":total,"completed":completed,"incomplete":incompleted,'sum':sum})
    

class Reset_Password(View):

    def get(self,request):

        form = ForgetForm

        return render(request,"reset.html",{'form':form})
    
    def post(self,request):

        form = ForgetForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")

            email = form.cleaned_data.get("email")

            password = form.cleaned_data.get("new_password")

            data = User.objects.get(username = username ,email = email)

            if data:

                data.password = make_password(password)

                data.save()

            return redirect("signin")


    
    