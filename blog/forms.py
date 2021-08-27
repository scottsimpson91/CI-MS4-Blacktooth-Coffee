from django import forms
from .models import Post, Comment


class BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'slug', 'intro', 'body']

    def clean_title(self):
        title = self.cleaned_data.get('title')

        for instance in Post.objects.all():
            if instance.title == title:
                raise forms.ValidationError(title + ' already exists.\
                                            Please edit the form')
        return title

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')

        for instance in Post.objects.all():
            if instance.slug == slug:
                raise forms.ValidationError(slug + ' already exists.\
                                            Please edit the form')
        return slug

    def clean_intro(self):
        intro = self.cleaned_data.get('intro')

        for instance in Post.objects.all():
            if instance.intro == intro:
                raise forms.ValidationError('This record already exists.\
                                            Please edit the form')
        return intro

    def clean_body(self):
        body = self.cleaned_data.get('body')

        for instance in Post.objects.all():
            if instance.body == body:
                raise forms.ValidationError('This record already exists.\
                                            Please edit the form')
        return body


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
