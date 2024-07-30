from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Post, Author
from .forms import SimpleForm, AuthorForm
from django.forms import modelform_factory
from django.views.generic import ListView


class PostListView(ListView):
    model = Post


@require_GET
def new_page(request):
    posts = Post.objects.all() 
    return HttpResponse(f"<h1>ЧТо-то не так с запросом время {posts[0].content} {id}</h1>")


def redirect_to_index(request):
    print(request.headers)
    return HttpResponseRedirect(reverse('mainapp:home'))

@require_GET
def smsform(request):
    return render(request, 'mainapp/simpleForm.html')

@require_POST
def send(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    print(name, email, message)
    return HttpResponseRedirect(reverse('mainapp:home'))


@require_http_methods(['GET', 'POST'])
def my_form(request):
    if request.method == "POST":
        form = SimpleForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('mainapp:home'))
    else:
        form = SimpleForm()
    return render(request, "mainapp/simpleForm.html", {'form' : form})


@require_http_methods(['GET', 'POST'])
def author_form(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:home'))
    else:
        form = AuthorForm()
    return render(request, "mainapp/simpleForm.html", {'form' : form})


@require_http_methods(['GET', 'POST'])
def author_edit_form(request, author_id):
    author = Author.objects.get(pk=author_id)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:home'))
    else:
        form = AuthorForm(instance=author)
    return render(request, "mainapp/simpleForm.html", {'form' : form, 'author': author})


def my_custom_page_not_found_view(request, ex):
    return render(request, '404.html', status=404)

def my_custom_page_server_error(request):
    return render(request, '404.html')

