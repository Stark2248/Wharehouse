from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
import bcrypt
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def admin(request):
    return render(request, 'home/adminuser.html')

def adminsave(request):

    message = " not saved "

    if Users.objects.count > 0 :
        users = Users.objects.all()
        for i in users:
            if i.username == request.POST.get("username") :
                message = " username already in the database. please provide any other unique username."
                return render(request, 'home/adminuser.html', {'message': message} )
    
    password=bytes(request.POST.get("password"),encoding='utf-8')

    salt=bcrypt.gensalt()

    hashed_pass= bcrypt.hashpw(password,salt)

    user= Users(username=request.POST.get("username"), name=request.POST.get("name"), password=hashed_pass )
    user.save()
    message="data saved successfully"

    return render(request, 'home/adminuser.html', {'message': message} )



