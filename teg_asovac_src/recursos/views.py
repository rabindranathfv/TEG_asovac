# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#import settings
from django.conf import settings
# import para envio de correo
from django.core.mail import send_mail

# Create your views here.
def recursos_pag(request):
    context = {
        "nombre_vista": 'recursos'
    }
    return render(request,"test_views.html",context)