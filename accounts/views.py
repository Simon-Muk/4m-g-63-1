from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout

from .forms import RegisterForm, LoginForm


def register_view(request):

    form = RegisterForm(request.POST or None,
                        request.FILES or None)

    if form.is_valid():

        user = form.save()

        login(request, user)

        return redirect('/')

    return render(request,
                  'accounts/register.html',
                  {'form': form})


def login_view(request):

    form = LoginForm(request,
                     data=request.POST or None)

    if form.is_valid():

        user = form.get_user()

        login(request, user)

        return redirect('/')

    return render(request,
                  'accounts/login.html',
                  {'form': form})


def logout_view(request):

    logout(request)

    return redirect('/')