from django.shortcuts import render, redirect, reverse
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BlogForm, CommentForm


def blog(request):
    """ A view to show the blog/brewtorials page """

    posts = Post.objects.all()

    return render(request, 'blog/blog.html', {'posts': posts})


def blog_detail(request, slug):
    """ A view to show individual blog/brewtorials page and comments """

    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('blog_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/blog_detail.html', {'post': post, 'form': form})


@login_required
def add_post(request):
    """ Add a post to the blog """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('blog_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
