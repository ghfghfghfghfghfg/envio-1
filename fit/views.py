from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from fit.models import Post 
from fit.forms import UsuarioForm
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")


tdee = 0
def add(request):
    genero = request.POST["genero"]
    anos = float(request.POST["anos"])
    altura = float(request.POST["altura"])
    peso = float(request.POST["peso"])
    pescoço = float(request.POST["pescoço"])
    cintura = float(request.POST["cintura"])
    quadril = float(request.POST["quadril"])
    objetivo = request.POST["objetivo"]
    atividade = request.POST["atividade"]


    if genero == 1:
        tdee = float((13.67*peso)+(5*altura)-(6.76* anos)+66.5)
        tdee_semana = float(tdee*7)
    else:
        tdee = float((9.56*peso)+(1.85*altura)-(4.68* anos)+665)
        tdee_semana = float(tdee*7)
    imc = peso / (altura*altura)
    tupla = (tdee,tdee_semana,imc)
    return render(request,"output.html", {"tupla":tupla})

def user(request):
    return render(request,"user.html")
    
def signup(request):
    return render(request,"sign-up.html")

def calculadora(request):
    return render(request,"calculadora.html")

def blog(request):
    posts = Post.objects.all()
    return render(request,"blog.html", {'posts':posts})

def sobrenos(request):
    return render(request,"sobre-nos.html")

def postagemblog(request, post_id):
    post =Post.objects.get(pk=post_id)
    return render(request,"postagem-blog.html",{'post':post})

class UsuarioCreate(CreateView):
    template_name = "sign-up.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)

        context['botao'] = "cadastro"

        return context
