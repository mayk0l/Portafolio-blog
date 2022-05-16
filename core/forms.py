from django import forms
from django.forms import ModelForm
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['idBlog', 'name', 'email', 'body']