from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Product


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль.')
    return render(request, 'orders/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Регистрация прошла успешно!')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Ошибка регистрации: {e}')
        else:
            messages.error(request, 'Пароли не совпадают.')

    return render(request, 'orders/register.html')

@login_required()
def product_list(request):
    products = Product.objects.all()  # Получаем все продукты
    return render(request, 'orders/product_list.html', {'products': products})
