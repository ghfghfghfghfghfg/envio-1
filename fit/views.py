from django.http import HttpResponse
from django.shortcuts import render
from fit.forms import calforms
from fit.models import Post 
# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def output(request):
    return render(request,"output.html")

def user(request):
    return render(request,"user.html")
    
def signup(request):
    return render(request,"sign-up.html")

def calculadora(request):
    if request.method == 'POST':
        form = calforms(request.POST) 
        if form.is_valid():
            form.save()
            form = calforms()
    else:
        form = calforms()
    return render(request,"calculadora.html", { 'form' : form})

def blog(request):
    posts = Post.objects.all()
    return render(request,"blog.html", {'posts':posts})

def sobrenos(request):
    return render(request,"sobre-nos.html")

def postagemblog(request, post_id):
    post =Post.objects.get(pk=post_id)
    return render(request,"postagem-blog.html",{'post':post})
    