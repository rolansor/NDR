from django.conf.urls import url
from basedatos import views

urlpatterns = [
    url(r'^recibirjson[/]?$',views.recibirjson, name='recibir_json'),

]