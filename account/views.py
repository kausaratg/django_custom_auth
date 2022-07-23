from django.shortcuts import render
from .forms import UserRegistration, UserLogin 
from .models import MyUser
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):
    user_form = UserRegistration()
    if request.POST:
        form_get = UserRegistration(request.POST)
        if form_get.is_valid():
            form_get.save()
            return redirect('my_login')
    context = {'user_form':user_form}
    return render(request, 'accounts/index.html', context)

def my_login(request):
    user_form = UserLogin()
    context = {'user_form': user_form}
    if request.method == 'POST':
            form_check = UserLogin(request.POST)
            if form_check.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('register')
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('my_login')

