from django.shortcuts import render, redirect, reverse
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BlogForm


def blog(request):
    """ A view to show the blog/brewtorials page """

    posts = Post.objects.all()

    return render(request, 'blog/blog.html', {'posts': posts})


def blog_detail(request, slug):
    """ A view to show individual blog/brewtorials page and comments """

    try:
        post = Post.objects.get(slug=slug)

    except Post.DoesNotExist:
        messages.error(request, 'Sorry, we could not find that post')
        return redirect(reverse('blog'))

    return render(request, 'blog/blog_detail.html', {'post': post})


@login_required
def add_post(request):
    """ Add a post to the blog """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('blog_detail', args=[post.slug]))
        else:
            messages.error(
                request,
                'Failed to add post. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):
    """ View to edit Blog/Brewtorials Post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    try:
        post = Post.objects.get(slug=slug)

    except Post.DoesNotExist:
        messages.error(request, 'Sorry, we could not find that post')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('blog_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to update post. Please ensure \
                the form is valid.')
    else:
        form = BlogForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, slug):
    """ View to delete Blog/Brewtorials Post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    try:
        post = Post.objects.get(slug=slug)

    except Post.DoesNotExist:
        messages.error(request, 'Sorry, we could not find that post')
        return redirect(reverse('home'))

    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
