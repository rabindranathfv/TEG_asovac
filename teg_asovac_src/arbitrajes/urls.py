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
    url(r'^listado-trabajos/$',views.listado_trabajos, name='listado'),
    url(r'^listado-trabajos/detalles/$',views.detalles_resumen, name='detalles_resumen'),
    url(r'^$', views.arbitrajes_pag, name= 'arbitrajes'),
    url(r'^dashboard/admin/referee/list/$',views.referee_list,name='referee_list'),
    url(r'^dashboard/admin/referee/edit/$',views.referee_edit,name='referee_edit'),
    url(r'^dashboard/admin/arbitrations/areas/subareas/$',views.areas_subareas,name='arbitrations_areas/subareas'),

]