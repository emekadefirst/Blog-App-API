from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import BlogPost, Comment
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
UserModel = get_user_model()


class BlogPostSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = BlogPost
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
            
