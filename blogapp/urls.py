from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.Test),
    path('get-all-post/', views.all_posts),
    path('posts/<str:model_name>/<int:pk>/comments/',
         views.post_comments, name='post-comments'),
   	path('signup', views.signup, name='register'),
   	path('login', views.login, name='login'),
    path('user', views.user, name='user'),
]
# http://127.0.0.1:8000//posts/blogpost/1/comments/ to post commnet on individual post
# http://127.0.0.1:8000/test/ test page 
# http://127.0.0.1:8000/get-all-post/ To get all post
