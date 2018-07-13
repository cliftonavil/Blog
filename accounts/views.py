from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('**************11111*********')
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('artiles:list')
    else:
        form = UserCreationForm()
        print('here******************')
    return render(request,'accounts/signup.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('artiles:list')
    else:
        form = AuthenticationForm()
        print('*************************')
    return render(request,'accounts/login.html',{'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('artiles:list')