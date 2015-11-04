from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from blog.models import Post

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for Django User model
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name')

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for blog post
    """
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'featured', 'user')
