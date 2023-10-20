from django.contrib import admin
from .models import BlogPost, Comment, Category


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'status', 'audio',
                    'image', 'video', 'category', 'date_published']
   

class CommentAdmin(admin.ModelAdmin):
    # Replace 'post' with 'blog_post'
    list_display = ('author', 'blog_post', 'created_at')


# , ' date_commented'
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


# class TokenAdmin(admin.ModelAdmin):
#     list_display = ['user', 'token', 'created_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
# admin.site.register(Token, TokenAdmin)

