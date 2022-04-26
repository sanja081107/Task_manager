from django.contrib import admin
from .models import Comment, Post, Category

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)


