from django.urls import path
from . import views
from blog.views import blog_detail, add_post, edit_post, delete_post

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_post/', add_post, name='add_post'),
    path('edit/<slug:slug>/', edit_post, name='edit_post'),
    path('delete/<slug:slug>/', delete_post, name='delete_post'),
    path('<slug:slug>/', blog_detail, name='blog_detail'),
]
