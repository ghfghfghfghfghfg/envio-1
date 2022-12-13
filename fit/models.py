from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  
from ckeditor_uploader.fields import RichTextUploadingField  
from django.contrib.auth.models import User
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

