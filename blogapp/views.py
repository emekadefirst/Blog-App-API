from django.contrib.auth import get_user_model, login, logout, authenticate
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost
from django.contrib.auth.models import User
from .serializers import BlogPostSerializer, CommentSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def Test(request):
    return Response({"Success": "Access graneted"})

@api_view(['GET'])
def all_posts(request):
    get_posts = BlogPost.objects.all()
    serializer = BlogPostSerializer(get_posts, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def post_comments(request, model_name, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'GET':
        # Return comments for the specific post
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        data['post'] = pk  # Associate the comment with the post
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Comment successfully posted"}, status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(["POST"])
def signup(request):

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=request.data['username'])
      
        serializer = UserSerializer(user)

        data = {
            "user": serializer.data,
        }

        return Response(data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
    
@api_view(["POST"])
def login(request):
    data = request.data
    authenticate_user = authenticate(username=data['username'], password=data['password'])
    
    if authenticate_user is not None:
        user = User.object.get(username=data['username'])
        serializer = UserSerializer(user)
    return Response({"message": "login"})

@api_view(['GET', 'POST'])
def user(request):

    return Response({"message": "logout up page"})
