from django.shortcuts import render, redirect
# from django.urls import reverse_lazy

from .forms import CommentForm
from .models import Post
from django.views.generic import ListView
from contact.forms import CantactForm
from django.core.paginator import Paginator


# Create your views here.


def home(request):
    form = CantactForm(request.POST or None)
    object_list = Post.objects.all()[:5]
    if form.is_valid():
        form.save()
        return redirect('/#Contact')
    context = {
        'form': form,
        'object_list': object_list
    }

    return render(request, 'base.html', context)


def postlar(request):
    form = CantactForm(request.POST or None)
    object_list = Post.objects.all()
    if form.is_valid():
        form.save()
        return redirect('/#Contact')
    context = {
        'form': form,
        'object_list': object_list
    }

    return render(request, 'postlar.html', context)


def detail(request, pk):
    form = CommentForm(request.POST or None)
    object_list = Post.objects.get(id=pk)
    url = request.META.get("HTTP_REFERER")
    if form.is_valid():
        var = form.save(commit=False)
        var.post = object_list
        var.save()
        return redirect(url)
    context = {
        'form': form,
        'post': object_list
    }

    return render(request, 'detail.html', context)


# def pagination(request):
#     post_list = Post.objects.all()
#     p = Paginator(Post.objects.all(), 2)
#     page = request.GET.get('page')
#     posts = p.get_page(page)
#
#     context = {
#         'post_list': post_list,
#         'posts': posts
#     }
#
#     return render(request, 'base.html', context)


class BlogListView(ListView):
    model = Post
    template_name = 'base.html'


class MalumotListView(ListView):
    model = Post
    template_name = 'malumot/info.html'


