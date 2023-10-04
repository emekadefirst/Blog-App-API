from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.Test),
    path('get-all-post/', views.all_posts),
    path('posts/<str:model_name>/<int:pk>/comments/',
         views.post_comments, name='post-comments')

]