"""web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.autores_pag, name= 'autores'),


    url(r'^administrador/crear-autor/$',views.admin_create_author,name='admin_create_author'),
    url(r'^crear-universidad/$',views.create_university_modal, name='create_university_modal'),
    url(r'^listar-autores/$',views.authors_list,name='authors_list'),
    url(r'^editar-autor/(?P<autor_id>\d+)/$',views.author_edit,name='author_edit'),
    url(r'^importar-excel/$',views.load_authors_modal,name='load_authors_modal'),

    url(r'^generar-certificado/$', views.generar_certificado, name = 'generar_certificado'),
    
    url(r'^postular-trabajo/(?P<trabajo_id>\d+)/$', views.postular_trabajo, name= 'postular_trabajo'),
    url(r'^detalles-rechazo/(?P<factura_id>\d+)/$',views.detalles_rechazo_pago, name='detalles_rechazo_pago'),   
    url(r'^postular-trabajo/pagador/(?P<autor_trabajo_id>\d+)/(?P<step>\d+)/$', views.postular_trabajo_pagador_modal, name= 'postular_trabajo_pagador_modal'),
    url(r'^editar-perfil/(?P<user_id>\d+)/$',views.author_edit_modal,name='author_edit_modal'),
    url(r'^detalles/(?P<autor_id>\d+)/$',views.author_details,name='author_details'), 
           


    url(r'^postular-trabajo/detalles-pago/(?P<pagador_id>\d+)/$', views.detalles_pago, name= 'detalles_pago'),

    #CRUD Universidades
    url(r'^listar-universidades/$',views.universitys_list,name='universitys_list'),
    url(r'^obtener-universidades/$',views.list_universitys ,name='list_universitys'), #Esta es para obtener los datos de la bootstrap table
    url(r'^borrar-universidad/(?P<university_id>\d+)/$',views.delete_university,name='delete_university'),
    url(r'^detalles-universidad/(?P<university_id>\d+)/$',views.details_university,name='details_university'),
    url(r'^editar-universidad/(?P<university_id>\d+)/$',views.edit_university,name='edit_university'),
    url(r'^admin-crear-universidad/$',views.create_university,name='create_university'),
   
    #Import de autores
    url(r'^load-authors-data$',views.list_authors,name='list_authors'),
    #Export de autores
    url(r'^export-authors$',views.export_authors,name='export_authors'),
    #Formato de import de autores
    url(r'^format-authors$',views.format_import_authors,name='format_import_authors'),
]