from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    my_title = "hello there..."
    context = {"title": my_title}
    return render(request, "hello.html", context)

def about_page(request):
    return render(request, "about.html", {"title":"About page"})

def contact_page(request):
    return render(request, "hello.html", {"title":"contact us"})

def example_page(request):
    context = {"title":"Example"}
    template_name = "hello.html"
    template_obj = get_template(template_name)
    render_item = template_obj.render(context)
    return HttpResponse(render_item)