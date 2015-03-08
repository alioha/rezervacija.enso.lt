from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

from modules.reservation.forms import SignupForm, LoginForm
from modules.reservation.models import UserName


@login_required
def events(request):
    """Landing view"""
    return HttpResponse("")


def account_create(request):
    """Create account view"""
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user_name = UserName()
            user_name.save()
            user = User.objects.create_user(username=user_name.id, email=form.cleaned_data["email"],
                                            password=form.cleaned_data["password1"])
            return render(request, "account/create_success.html", {"user": user})
    else:
        form = SignupForm()

    return render(request, "account/create.html", {"form": form})


def account_login(request):
    """Login account"""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            login(request=request, user=user)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, "account/login.html", {"form": form})


@login_required
def account_logout(request):
    """Logout account"""
    logout(request)
    return redirect('/')
