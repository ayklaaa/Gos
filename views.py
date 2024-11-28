from sqlite3 import IntegrityError
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login as user_login, logout as user_logout, logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from .models import MInstitutions, MService, MAppointments, MStaatus

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AppointmentForm


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin:index')  # Перенаправляем в админку после успешного сохранения
    else:
        form = AppointmentForm()
    return render(request, 'form.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def test(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем заявку в базу данных
            return redirect('/')  # Перенаправляем после отправки формы
    else:
        form = AppointmentForm()

    institutions = MInstitutions.objects.all()  # Извлекаем все учреждения
    services = MService.objects.all()  # Извлекаем все услуги

    appointments = MAppointments.objects.all()  # Извлекаем все заявки

    return render(request, 'test.html', {
        'institutions': institutions,
        'services': services,

        'appointments': appointments,
        'form': form,
    })


def login_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        usr = authenticate(request, username=login, password=password)
        if usr is not None:
            user_login(request, usr)
            return HttpResponseRedirect('registration/profile')
        else:
            return render(request, 'registration/login.html')


def reg_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Имя
        surname = request.POST.get('surname')  # Фамилия
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            try:
                # Создаем пользователя
                user = User.objects.create_user(username=username, password=password)
                user.first_name = name  # Сохраняем имя
                user.last_name = surname  # Сохраняем фамилию
                user.save()

                # Аутентификация пользователя
                usr = authenticate(request, username=username, password=password)
                if usr is not None:
                    user_login(request, usr)
                    return HttpResponseRedirect('profile/')
                else:
                    return render(request, 'auth/reg.html', {'error': 'Authentication failed.'})
            except IntegrityError:
                # Если пользователь с таким именем уже существует
                return render(request, 'auth/reg.html', {'error': 'Username already exists.'})
            except Exception as e:
                # Обработка других исключений
                return render(request, 'auth/reg.html', {'error': str(e)})
        else:
            return render(request, 'auth/reg.html', {'error': 'Passwords do not match.'})
        context = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        # Если метод не POST, просто рендерим страницу регистрации
    return render(request, 'auth/reg.html', context)

def custom_logout_view(request):
    logout(request)  # Удаляем данные из сессии
    return redirect('/')  # Перенаправляем на главную страницу
# def reg_view(request):
#     if request.method == 'POST':
#         login = request.POST.get('login')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#
#         if password1 == password2:
#             try:
#                 # Создаем пользователя с правильными аргументами
#                 User.objects.create_user(username=login, password=password1)
#                 usr = authenticate(request, username=login, password=password1)
#
#                 if usr is not None:
#                     user_login(request, usr)
#                     return HttpResponseRedirect('/')  # Перенаправляем на главную страницу
#                 else:
#                     return render(request, 'auth/reg.html', {'error': 'Authentication failed.'})
#             except Exception as e:
#                 return render(request, 'auth/reg.html', {'error': str(e)})
#         else:
#             return render(request, 'auth/reg.html', {'error': 'Passwords do not match.'})
#
#     # Если метод не POST, просто рендерим страницу регистрации
#     return render(request, 'auth/reg.html')


def form(request):
    return render(request, 'form.html')


@login_required
def profile_view(request):
    return render(request, 'registration/profile.html', {'user': request.user})
