from django.shortcuts import render
from .forms import CantactForm
from django.views.generic import ListView


# Create your views here.


def contact(request):
    form = CantactForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }

    return render(request, 'contact.html', context)
