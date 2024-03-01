from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def signin(request):
    if request.method == "POST":
        email = request.POST['uname']
        passwd = request.POST['passwd']
        user = authenticate(username=email,password=passwd)
        if user is not None:
            login(request,user)
            return redirect('add_file')
        else:
            print("Invalid User")
    return render(request,'accounts/login.html')

def signout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        # password = request.POST['passwd']
        company = request.POST['company']

        emp = Account.objects.create_masteruser(first_name=fname,last_name=lname,email=email,company_name=company)
        password = '123456'
        emp.set_password(password)
        emp.save()
        print("Emp saved")
    return render(request,'accounts/login.html')
    