from django import forms
from .models import Post


class BlogForm(forms.ModelForm):
    """ Form to add new Blog/Brewtorials Post """

    class Meta:
        model = Post
        fields = ['title', 'slug', 'intro', 'body']
