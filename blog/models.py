from django.db import models
from django.core.validators import RegexValidator


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, validators=[RegexValidator(regex='^.{3}$', message='Minimum length of 3 characters', code='nomatch')])
    email = models.EmailField()
    body = models.TextField(validators=[RegexValidator(regex='^.{5}$', message='Minimum length of 5 characters', code='nomatch')])
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.name
