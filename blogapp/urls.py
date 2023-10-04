from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.Test),
    path('get-all-post/', views.all_posts),
    path('posts/<str:model_name>/<int:pk>/comments/',
         views.post_comments, name='post-comments'),
   	path('register', views.UserRegister.as_view(), name='register'),
   	path('login', views.UserLogin.as_view(), name='login'),
   	path('user', views.UserView.as_view(), name='user'),
]
# http://127.0.0.1:8000//posts/blogpost/1/comments/ to post commnet on individual post
# http://127.0.0.1:8000/test/ test page 
# http://127.0.0.1:8000/get-all-post/ To get all post
