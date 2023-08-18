
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm, LoginForm


def registration(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                print(request, error)
    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name='users/register.html.',
        context={'form': form}
    )


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect("/")
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')
