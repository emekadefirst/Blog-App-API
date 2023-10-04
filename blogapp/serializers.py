from rest_framework import serializers
from .models import BlogPost, Comment


class BlogPostSerializer(serializers.ModelSerializer):
    
    category = serializers.CharField(source='category.name')

    class Meta:
        model = BlogPost
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
