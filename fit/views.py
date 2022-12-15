from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from fit.models import Post 
from fit.forms import UsuarioForm
from django.urls import reverse_lazy
from fit.models import Perfil
from django.shortcuts import get_object_or_404
import math
# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")


tdee = 0
def add(request):

    
    genero = int(request.POST["genero"])
    anos = str(request.POST["anos"])
    altura = str(request.POST["altura"])
    peso = str(request.POST["peso"])
    pescoço = str(request.POST["pescoço"])
    cintura = str(request.POST["cintura"])
    quadril = str(request.POST["quadril"])
    objetivo = str(request.POST["objetivo"])
    atividade = int(request.POST["atividade"])


    if anos == "" or altura == "" or peso == "" or pescoço == "" or cintura == "" or  quadril == "":
            return render(request,"calculadora.html")

    anos = float(request.POST["anos"])
    altura = float(request.POST["altura"])
    peso = float(request.POST["peso"])
    pescoço = float(request.POST["pescoço"])
    cintura = float(request.POST["cintura"])
    quadril = float(request.POST["quadril"])
    imc = peso / (altura*altura)


    if genero == 1:
        tmb = round(float((13.67*peso)+(5*altura)-(6.76* anos)+66.5))
        if atividade ==1:
            tdee = round(float(tmb*1.2))
        elif atividade ==2:
            tdee = round(float(tmb*1.375))
        elif atividade ==3:
            tdee = round(float(tmb*1.55))
        elif atividade ==4:
            tdee =round(float(tmb*1.725))
        else:
            tdee = round(float(tmb*1.9))

        tdee_semana = round(float(tdee*7))
        tdee_sedentario = round(float(tmb*1.2))
        tdee_ExeLeve = round(float(tmb*1.375))
        tdee_ExeMOderado = round(float(tmb*1.55))
        tdee_ExePesado = round(float(tmb*1.725))
        tdee_atleta = round(float(tmb*1.9))

        



    else:
        tmb = float((9.56*peso)+(1.85*altura)-(4.68* anos)+665)
        if atividade ==1:
            tdee = float(tmb*1.2)
        elif atividade ==2:
            tdee = float(tmb*1.375)
        elif atividade ==3:
            tdee =float(tmb*1.55)
        elif atividade ==4:
            tdee = float(tmb*1.725)
        else:
            tdee = float(tmb*1.9)
        tdee_semana = float(tdee*7)
        tdee_sedentario = float(tmb*1.2)
        tdee_ExeLeve =float(tmb*1.375)
        tdee_ExeMOderado =float(tmb*1.55)
        tdee_ExePesado =float(tmb*1.725)
        tdee_atleta =float(tmb*1.9)

        
    BFPm = round(float((1.20 * imc) + (0.23 * anos) - 16.2))
    ffmim =  round(float( peso * (1-(BFPm/100)) ))
    BFPh = round(float((1.20 * imc) + (0.23 * anos) - 5.4))
    ffmi =  round(float((peso*(1-(BFPh/100)))/altura*altura))
    cutting = round(float(tdee - 500))
    bulking = round(float(tdee + 500))
    manutenção1= round(float(tdee*0.55)/4)
    manutenção2= round(float(tdee*0.25)/4)
    manutenção3= round(float(tdee*0.20)/9)
    cutting1= round(float(cutting*0.55)/4)
    cutting2= round(float(cutting*0.25)/4)
    cutting3= round(float(cutting*0.20)/9)
    bulking1= round(float(bulking*0.55)/4)
    bulking2= round(float(bulking*0.25)/4)
    bulking3= round(float(bulking*0.20)/9)

    manutenção11= round(float(tdee*0.45)/4)
    manutenção21= round(float(tdee*0.25)/4)
    manutenção31= round(float(tdee*0.30)/9)
    cutting11= round(float(cutting*0.45)/4)
    cutting21= round(float(cutting*0.25)/4)
    cutting31= round(float(cutting*0.30)/9)
    bulking11= round(float(bulking*0.45)/4)
    bulking21= round(float(bulking*0.25)/4)
    bulking31= round(float(bulking*0.30)/9)

    manutenção111= round(float(tdee*0.45)/4)
    manutenção211= round(float(tdee*0.35)/4)
    manutenção311= round(float(tdee*0.20)/9)
    cutting111= round(float(cutting*0.45)/4)
    cutting211= round(float(cutting*0.35)/4)
    cutting311= round(float(cutting*0.20)/9)
    bulking111= round(float(bulking*0.45)/4)
    bulking211= round(float(bulking*0.35)/4)
    bulking311= round(float(bulking*0.20)/9)



        
    tupla = (tdee,tdee_semana,tmb,tdee_sedentario,tdee_ExeLeve,tdee_ExeMOderado,tdee_ExePesado,
    tdee_atleta,imc,BFPm,ffmim,BFPh,ffmi,cutting,bulking,
    manutenção1,manutenção2,manutenção3,cutting1,cutting2,cutting3,bulking1,bulking2,bulking3,
    manutenção11,manutenção21,manutenção31,cutting11,cutting21,cutting31,bulking11,bulking21,bulking31,
    manutenção111,manutenção211,manutenção311,cutting111,cutting211,cutting311,bulking111,bulking211,bulking311)
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
    template_name = "atualizar.html"
    model = Perfil
    fields = ['peso','altura']
    success_url = reverse_lazy("calculadora")


    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil,usuario=self.request.user)
        return self.object

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)

        context["botao"] = "atualizar"

        return context

        ###