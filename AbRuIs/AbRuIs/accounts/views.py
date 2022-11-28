from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, forms


def registr(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # phone_number = request.POST.get('phone_number')
        if password == password2:
            pass
            user = User.objects.filter(username=username)
            if not user.exists():
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz")
                return redirect('/accounts/sign-in/')
            messages.success(request, "Ushbu username allaqachon ro'yxatdan o'tkazilgan")
            return redirect('/accounts/signup/')
        messages.success(request, "Parollar mos emas")
        return redirect('/accounts/signup/')

    return render(request, 'registration/signup.html')


def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username yoki password notug`ri')
            return redirect('/accounts/sign-in/')
    context = {

    }
    return render(request, 'registration/login.html', context)


#
#
def logout(request):
    logout(request)
    return redirect('/')


def logout1(request):
    context = {
    }
    return render(request, 'registration/chiqish.html', context)
