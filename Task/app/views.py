from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def Login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        user_em = request.POST['UserName']
        user_ep = request.POST['Password1']
        a = authenticate(username=user_em, password=user_ep)
        if a is not None:
            login(request, a)  # Use the renamed function
            return HttpResponse('Login Successfully')
        else:
            return redirect('/')
    return render(request,'login.html')

def Register(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        
        UserName=request.POST['UserName']
        Name=request.POST['Name']
        Email=request.POST['UserEmail']
        PassWord=request.POST['UserPassword']
        obj=User.objects.create(username=UserName,first_name=Name,email=Email)
        obj.set_password(PassWord)
        obj.save()
        return redirect('/')
