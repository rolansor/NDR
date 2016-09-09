from django.conf.urls import url
from reportes import views

urlpatterns = [
    url(r'^geo_reportes[/]?$', views.reportes_geograficos, name='reportes_geograficos'),
    url(r'^gra_reportes[/]?$', views.reportes_graficos, name='reportes_graficos'),
    url(r'^doc_reportes/preparacion[/]?$', views.reportes_preparacion, name='reportes_fisicos'),
    url(r'^doc_reportes/informacion[/]?$', views.reportes_informacion, name='reportes_fisicos'),
    url(r'^doc_reportes/medidas[/]?$', views.reportes_medidas, name='reportes_fisicos'),
    url(r'^doc_reportes/presion[/]?$', views.reportes_presion, name='reportes_fisicos'),
    url(r'^doc_reportes/laboratorio[/]?$', views.reportes_laboratorio, name='reportes_fisicos'),
    url(r'^doc_reportes/personalizado[/]?$', views.reportes_personalizado, name='reportes_fisicos'),

]