from django.urls import path
from . import views
from blog.views import blog_detail, add_post

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_post/', add_post, name='add_post'),
    path('<slug:slug>/', blog_detail, name='blog_detail'),
]
