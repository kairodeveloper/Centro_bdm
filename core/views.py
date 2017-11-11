from django.shortcuts import render, render_to_response, HttpResponseRedirect
from .models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse

# Create your views here.
def home(request):
    noticias = Noticia.objects.all()
    noticias = noticias[::-1]
    recentes = noticias[0:3]

    return render(request, 'core/home.html', {'recentes':recentes})


def atividades(request):
    return render(request, 'core/atividades.html', {})

def noticias(request):
    news = Noticia.objects.all()
    news = news[::-1]
    paginator = Paginator(news,5)

    # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        news = paginator.page(page)
    except (EmptyPage, InvalidPage):
        news = paginator.page(paginator.num_pages)

    return render_to_response('core/noticias.html',{'news':news})

def quemsomos(request):
    participantes = Participante.objects.all()
    return render(request, 'core/quemsomos.html',{'participantes':participantes})

def contato(request):
    return render(request, 'core/contato.html', {})