
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse
from django.views.generic import UpdateView
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm, UserUpdateForm
from .models import CustomUser




def registration(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Пользователь {user} успешно зарегестрирован')
            print(type(messages), messages.success)
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
            messages.success(request, f'Вход {user} успешно выполнен')
            return redirect("/")
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


class Profile(UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'users/profile.html'


    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Данные профиля успешно изменены')
        return reverse('index',)



    # def get(self, request, username):
    #     data = CustomUser.objects.filter(username=username)
    #     context = {
    #         'data': data
    #     }
    #     return render(request, self.template_name, context)
