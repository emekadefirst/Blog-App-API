from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    blog_post = models.ForeignKey(
        'BlogPost', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.author.username} on {self.blog_post.title}"


class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    hashtag = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_post', blank=True)
    shares = models.PositiveIntegerField(default=0)
    image = models.FileField(upload_to="blog-post-media")
    video = models.FileField(upload_to='uploads/videos', blank=True)
    audio = models.FileField(upload_to='uploads/audios', blank=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.title

    def get_comment_count(self):
        return self.comments.count()
