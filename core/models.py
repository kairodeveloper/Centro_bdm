from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Evento(models.Model):
    pass


class Noticia(models.Model):
    cod_noticia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60, unique=True, default="Titulo noticia")
    autor = models.CharField(max_length=60, default="Autor noticia")
    texto = models.CharField(max_length=2000, default="Autor texto")
    categoria = models.CharField(max_length=40, default="Espiritismo")
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)
    acessos = models.IntegerField(default=0)


