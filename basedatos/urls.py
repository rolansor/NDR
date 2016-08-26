from django.conf.urls import url
from basedatos import views

urlpatterns = [
    url(r'^recibirjson[/]?$',views.recibirjson, name='recibir_json'),
    url(r'^leerjson[/]?$',views.leer_json, name='recibir_json'),
    url(r'^encuestasubida[/]?$', views.leer_json, name='recibir_json'),
]