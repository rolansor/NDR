from django.conf.urls import url
from usuarios import views

urlpatterns = [
    url(r'^geo_reportes[/]?$', views.reportes_geograficos, name='reportes_geograficos'),
    url(r'^gra_reportes[/]?$', views.reportes_graficos, name='reportes_graficos'),
    url(r'^doc_reportes[/]?$', views.reportes_fisicos, name='reportes_fisicos'),

]