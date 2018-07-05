"""core_app URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from django.shortcuts import render
#import settings
from django.conf import settings
# import para envio de correo
from django.core.mail import send_mail
#import for use include
from django.conf.urls import include
#import para collect static y usar media
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    ## add routing using include in apps / The namespace allows for url tag convention to be used in templates.
    url(r'^', include('main_app.urls',      namespace='main_app')),
    url(r'^', include('arbitrajes.urls',    namespace='arbitrajes')),
    url(r'^', include('recursos.urls',      namespace='recursos')),
    url(r'^', include('seguimiento.urls',   namespace='seguimiento')),
    url(r'^', include('sesiones.urls',      namespace='sesiones')),
    url(r'^', include('trabajos.urls',      namespace='trabajos')),
    url(r'^', include('eventos.urls',       namespace='eventos')),
    url(r'^', include('autores.urls',       namespace='autores')),
    
]

# add config for link styles, for collectstatic
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)