from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer, CommentSerializer


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
