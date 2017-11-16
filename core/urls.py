from core import views
from django.conf.urls import url, include
from django.contrib.auth.views import login,logout
from django.conf import settings
from django.template.response import TemplateResponse


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^atividades$', views.atividades, name='atividades'),
    url(r'^noticias$', views.noticias, name='noticias'),
    url(r'^quemsomos$', views.quemsomos, name='quemsomos.css'),
    url(r'^contato$', views.contato, name='contato'),
    url(r'^galeria$', views.galeria, name='galeria')

]

