from django.shortcuts import render
from account.models import Account
from .models import File
# Create your views here.
def add_user(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        
        email = request.POST['email']
        user = Account.objects.create_user(first_name = fname,last_name=lname,email=email)
        passwd = '123456'
        user.set_password(passwd)
        user.save()
        print("User Dooe")
        return render(request,'add_user.html',{"msg":"User Added!"})
    return render(request,'add_user.html',)



def add_file(request):
    if request.method=='POST':
        file = request.FILES['file']
        file_name = request.POST['file_name']
        # users = request.POST['all_user']
        all_users = [x.email for x in Account.objects.all()]
        user_ids = []
        for x in all_users:
            user_ids.append(int(request.POST.get(x))) if request.POST.get(x) else print("hello")

        # print("--------")
        # print(file_name)
        # print(user_ids)
        # print("--------")

        new_file = File.objects.create(file =file,file_name=file_name)

        for x in user_ids:
            # print("--------")
            # print(x)
            new_file.has_access.add(Account.objects.get(id=x))
        new_file.save()
        return render(request,'add_file.html',{"msg":"File Added"})
    
    return render(request,'add_file.html',{"users":Account.objects.all()})


def all_files(request):
    # all_files = File.objects.all()
    all_files = File.objects.filter(has_access=request.user)
    context = {
        "all_files":all_files
    }   


    # file = File.objects.get(id=15)
    # users_with_access = file.user.all()
    # for user in users_with_access:
    #     print(user.email)
        
    return render(request,"all_files.html",context)


