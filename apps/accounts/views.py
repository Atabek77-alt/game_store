# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterView(CreateView):
    model = User
    template_name = 'base.html'
    form_class = RegisterForm
    success_url = '/login/'  # После регистрации, перенаправляем на страницу логина

    def form_valid(self, form):
        # Создаем нового пользователя
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        # Создаем пользователя
        user = User.objects.create_user(username=username, email=email, password=password)

        # Входим в систему после регистрации
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return redirect(self.success_url)
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import FormView
from .forms import LoginForm

class LoginView(FormView):
    template_name = 'base.html'  # Указываем, что используется base.html
    form_class = LoginForm
    success_url = '/'  # После успешного входа будет редирект на главную

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        # Авторизация пользователя
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('home')  # Перенаправляем на главную страницу после логина
            else:
                return HttpResponse('Этот пользователь заблокирован.')
        else:
            return HttpResponse('Такого пользователя не существует или данные неправильные.')
