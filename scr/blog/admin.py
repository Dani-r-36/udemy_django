from django.contrib import admin

# Register your models here.
from .models import BlogPost
from .models import Comment

admin.site.register(BlogPost)
admin.site.register(Comment)