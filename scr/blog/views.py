from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
# Create your views here.

from .models import BlogPost
from .forms_blog import BlogPostModelForm
from .forms_blog import CommentForm


def blog_post_list_view(request):
    qs = BlogPost.objects.all().published()#.filter(title__icontains='hello') #queryset -> list of python object
    template_name = 'blog/post_list.html'
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user = request.user)
        qs = (qs| my_qs).distinct()
    context = {'object_list': qs}
    return render(request, template_name,context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    print("inside")
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        print(request.FILES)
        print(request.POST)
        if 'image' in request.FILES:
            obj.image = form.cleaned_data['image']
        obj.save()
        form = BlogPostModelForm()
    print('after if')
    context = {"form":form}
    template_name = 'form.html'
    return render(request, template_name,context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    comment_form = CommentForm()
    if request.method =='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog_post = obj
            comment.author = request.user
            comment.save()
            print(comment.comment)
        else:
            print("comment is not valid")
            print(comment_form.errors)
    
    context = {'object_list':obj, 'comment_form':comment_form}
    template_name = 'blog/post_detail.html'
    return render(request, template_name,context)

@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {'form': form, 'title':f"Update {obj.title}"}
    return render(request, template_name,context)

@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog/post_delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {'object_list':obj}
    return render(request, template_name,context)