from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CantactForm
from django.views.generic import ListView


# Create your views here.


def contact(request):
    form = CantactForm(request.POST or None)
    url = request.META.get("HTTP_REFERER")
    if form.is_valid():
        form.save()
        messages.success(request, "Ushbu username allaqachon ro'yxatdan o'tkazilgan")
        return redirect(url)
    context = {
        'form': form
    }
    return render(request, 'base.html', context)
