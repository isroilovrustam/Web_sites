from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from contact.forms import CantactForm


# Create your views here.


def home(request):
    form = CantactForm(request.POST or None)
    object_list = Post.objects.all()
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        'object_list': object_list
    }

    return render(request, 'base.html', context)


# class BlogListView(ListView):
#     model = Post
#     template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
