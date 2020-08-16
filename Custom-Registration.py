from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('logged in!')
            return redirect("/beatbox/")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect("/accounts/login/")

    else:
        return render(request, 'login.html')
        
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if (len(username) < 12):
                if User.objects.filter(username=username).exists():
                    print('Username Taken')
                    messages.info(request, 'Username Already in Use')
                    return redirect('/accounts/register/')
                elif User.objects.filter(email=email).exists():   
                    print('Email Taken') 
                    messages.info(request, 'Email Already in Use')
                    return redirect('/accounts/register/')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name,)
                    user.save()
                    print('user created')
                    return redirect('/beatbox/')
            else:
                messages.info(request, "Username exceeds 12 Characters")
                return redirect('/accounts/register/')
        else:
            print('passwords dont match')
            messages.info(request, "Passwords don't match")
            return redirect('/accounts/register/')
        
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/beatbox/')