from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as gtl


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
        label="Введите пароль",
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        strip=False,
        widget=forms.PasswordInput,
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': gtl('Логин'),
            'first_name': gtl('Имя'),
            'last_name': gtl('Фамилия'),
            'email': gtl('Email'),
        }
        help_texts = {
            'username': None,
        }

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label='Логин', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Введите пароль', required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Извините, логин или пароль неверен. Проверьте правильность данных")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
