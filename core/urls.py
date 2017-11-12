from core import views
from django.conf.urls import url, include,handler404,handler500
from django.contrib.auth.views import login,logout
from django.conf import settings
from django.template.response import TemplateResponse 


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^atividades$', views.atividades, name='atividades'),
    url(r'^noticias$', views.noticias, name='noticias'),
    url(r'^quemsomos$', views.quemsomos, name='quemsomos'),
    url(r'^contato$', views.contato, name='contato'),
    url(r'^404$', views.error404, name='error404')
]
