from django.conf.urls import url
from usuarios import views

urlpatterns = [
    url(r'^ingreso[/]?$',views.ingreso, name='ingreso_usuarios'),
    url(r'^[/]?$', views.inicio, name='inicio'),

]