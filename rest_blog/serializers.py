from rest_framework import serializers
from core.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['idBlog', 'name', 'email', 'body']