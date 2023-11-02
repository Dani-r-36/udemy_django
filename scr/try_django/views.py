from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
    qs = BlogPost.objects.all()[:5]
    context = {'blog_list': qs}
    return render(request, "hello.html", context)

def about_page(request):
    return render(request, "about.html", {"title":"About page"})

def contact_page(request):
    # print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form = ContactForm()
        context = {"title":"contact us", "form":form}
    return render(request, "form.html", context)

def example_page(request):
    context = {"title":"Example"}
    template_name = "hello.html"
    template_obj = get_template(template_name)
    render_item = template_obj.render(context)
    return HttpResponse(render_item)