from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from fit.models import Post 
from fit.forms import UsuarioForm
from django.urls import reverse_lazy
from fit.models import Perfil
# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")


tdee = 0
def add(request):
    genero = int(request.POST["genero"])
    anos = float(request.POST["anos"])
    altura = float(request.POST["altura"])
    peso = float(request.POST["peso"])
    pescoço = float(request.POST["pescoço"])
    cintura = float(request.POST["cintura"])
    quadril = float(request.POST["quadril"])
    objetivo = request.POST["objetivo"]
    atividade = int(request.POST["atividade"])


    if genero == 1:
        tmb = float((13.67*peso)+(5*altura)-(6.76* anos)+66.5)
        tdee = tmb
        tdee_semana = float(tdee*7)

    else:
        tmb = float((9.56*peso)+(1.85*altura)-(4.68* anos)+665)
        tdee = tmb
        tdee_semana = float(tdee*7)
        tdee_sedentario = tmb*1.2
        tdee_ExeLeve =float(tmb*1.375)
        tdee_ExeMOderado =float(tmb*1.55)
        tdee_ExePesado =float(tmb*1.725)
        tdee_atleta =float(tmb*1.9)
        
    imc = peso / (altura*altura)
    tupla = str((tdee,tdee_semana,tmb,tdee_sedentario,tdee_ExeLeve,tdee_ExeMOderado,tdee_ExePesado,tdee_atleta,imc))
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

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Docente")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url


    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)

        context['botao'] = "cadastro"

        return context


class PerfilUpdate(UpdateView):
    template_name = "calculadora.html"
    model = Perfil
    fields = ['peso','altua']
    success_url = reverse_lazy("index.html")


    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)

        context["botao"] = "atualizar"

        return context