from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def home(request):
    return render(request, 'base.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['1st_pwd'] == request.POST['2nd_pwd']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['1st_pwd'])
            userprofile = UserProfile(user=user)
            userprofile.save()
            auth.login(request.user)
            return redirect('main:home')
        return render(request, 'logged/signup.html')
    else:
        return render(request, 'logged/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['1st_pwd']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:home')
        else:
            return render(request, 'logged/login.html', {'error' : 'username or password is incorrect. '})
    else:
        return render(request, 'logged/login.html')

def logout(request):
    auth.logout(request)
    return redirect('logged:login')