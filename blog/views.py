from django.shortcuts import render, redirect, reverse
from .models import Post


def blog(request):
    """ A view to show the blog/brewtorials page """

    posts = Post.objects.all()

    return render(request, 'blog/blog.html', {'posts': posts})


def blog_detail(request, slug):
    """ A view to show individual blog/brewtorials page """

    post = Post.objects.get(slug=slug)

    return render(request, 'blog/blog_detail.html', {'post': post})
