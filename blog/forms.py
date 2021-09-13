from django import forms
from .models import Post, Comment


class BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'slug', 'intro', 'body']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
