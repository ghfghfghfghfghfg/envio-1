from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  
from ckeditor_uploader.fields import RichTextUploadingField  
# Create your models here.


# blog model's
class Post(models.Model):
    titulo =models.CharField(max_length=255)
    resumo = RichTextField()
    conteudo = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    data_criacao = models.DateField(auto_now_add=True)
    #miniatura_img = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.titulo

SEXO = (
    ('M','Masculino'),
    ('F','Feminino'),
)

OBJETIVO = (
    ('Manter peso','Manter peso'),
    ('Perder peso (leve)','Perder peso (leve)'),
    ('Perde peso','Perde peso'),
    ('Ganhar peso (leve)','Ganhar peso (leve)'),
    ('Ganhar peso','Ganhar peso'),
)

ATIVIDADE = (
    ('Sedentario','Sedentario'),
    ('Levemente ativo','Levemente ativo'),
    ('Moderadamente','Moderadamente'),
    ('Muito ativo','Muito ativo'),
    ('Extremanente','Extremanente'),
)

class CalculadoraForms(models.Model):
    genero = models.CharField(choices=SEXO,max_length=30)
    anos = models.CharField(max_length=3)
    altura = models.CharField(max_length=3)
    peso = models.CharField(max_length=3)
    pescoco = models.CharField(max_length=3)
    cintura = models.CharField(max_length=3)
    quadril = models.CharField(max_length=3)
    objetivo = models.CharField(choices=OBJETIVO,max_length=30)
    atividade = models.CharField(choices=ATIVIDADE,max_length=30)
