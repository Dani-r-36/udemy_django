from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.

from .models import BlogPost


def blog_post_list_view(request):
    qs = BlogPost.objects.all()#.filter(title__icontains='hello') #queryset -> list of python object
    template_name = 'blog/post_list.html'
    context = {'object_list': qs}
    return render(request, template_name,context)


def blog_post_create_view(request):
    template_name = 'blog/post_create.html'
    context = {'form':None}
    return render(request, template_name,context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog/post_detail.html'
    context = {'object_list':obj}
    return render(request, template_name,context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog/post_update.html'
    context = {'object_list':obj, 'form': None}
    return render(request, template_name,context)

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog/post_delete.html'
    context = {'object_list':obj}
    return render(request, template_name,context)