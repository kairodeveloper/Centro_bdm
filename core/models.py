from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Participante(models.Model):
    cod_participante = models.AutoField(primary_key=True)
    nome_completo = models.CharField(max_length=60, default="Nome da Pessoa")
    email = models.CharField(max_length=60, default="pessoa@email.com")
    nome = models.CharField(max_length=20, default="Nome sobrenome")
    sobrenome = models.CharField(max_length=20, default="Nome sobrenome")
    descricao = models.CharField(max_length=150, default="descricao do que a pessoa faz na casa")
    imagem = models.FileField(upload_to="participantes/%Y/%m/%d")

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
    imagem_principal = models.FileField(blank=False, default="logo_centro.png",upload_to="noticias/%Y/%m/%d")


