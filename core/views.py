from django.shortcuts import render, render_to_response, redirect
from .models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .forms import *
from django.core.urlresolvers import reverse_lazy
from datetime import datetime

# Create your views here.
def home(request):
    noticias = Noticia.objects.all()
    noticias = noticias[::-1]
    recentes = noticias[0:3]

    eventos = EventoMes.objects.all()
    eventosDoMes = []

    dateNow = datetime.now()

    dateMonth = dateNow.month

    for i in eventos:
        if i.data.month==dateMonth:
            eventosDoMes.append(i)

    return render(request, 'core/home.html', {'recentes':recentes, 'eventos':eventosDoMes })


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

    if request.method=='POST':
        nome = request.POST.get('name-input')
        email = request.POST.get('email-input')
        mensagem = request.POST.get('message-input')

        if (is_null(nome)):
            return render(request, 'core/contato.html', {'cod':0})
        elif (is_null(email)):
            return render(request, 'core/contato.html', {'cod':0})
        elif (is_null(mensagem)):
            return render(request, 'core/contato.html', {'cod':0})
        else:
            my_send_email(nome, email, mensagem)
            return render(request, 'core/contato.html', {'cod':1})

    return render(request, 'core/contato.html', {'cod':-1})


def galeria(request):

    if request.method=='POST':
        form = ParticipanteForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            participantes = Participante.objects.all()

            return redirect(reverse_lazy('core:quemsomos'))
        return render(request, 'core/galeria.html', {'form':form})

    else:
        form = ParticipanteForm(request.POST, request.FILES)
        return render(request, 'core/galeria.html',{'form':form})



#NOT VIEWS
def my_send_email(nome, email, mensagem):
    import smtplib

    remetente = 'site.centro.bdm.no.reply@gmail.com'

    destinatario = 'kairoemannoel@hotmail.com'
    assunto = 'Site Centro Bezerra de Menezes'
    texto = 'Nome do visitante: %s' % nome+"\n"+"Email do visitante: %s" % email+"\nMensagem: "+mensagem

    msg = '\r\n'.join(['From: %s' % remetente,'To: %s' % destinatario,'Subject: %s' % assunto,'','%s' % texto])

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(remetente,senha)
    server.sendmail(remetente, destinatario, msg)
    server.quit()

def is_null(field):
    if(len(field)==0):
        return True
    return False

def handle_uploaded_file(f):
    destination = open('static/imagens/teste.jpg', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
