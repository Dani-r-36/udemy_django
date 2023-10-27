from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm

def home_page(request):
    my_title = "hello there..."
    context = {"title": my_title}
    return render(request, "hello.html", context)

def about_page(request):
    return render(request, "about.html", {"title":"About page"})

def contact_page(request):
    # print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
        context = {"title":"contact us", "form":form}
    return render(request, "form.html", context)

def example_page(request):
    context = {"title":"Example"}
    template_name = "hello.html"
    template_obj = get_template(template_name)
    render_item = template_obj.render(context)
    return HttpResponse(render_item)