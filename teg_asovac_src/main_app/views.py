# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, render_to_response
from .forms import MyLoginForm, CreateArbitrajeForm, RegisterForm, DataBasicForm

from django.db.models import Q
from decouple import config
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse
from .models import Rol,Sistema_asovac,Usuario_asovac

import random, string
# Global functions
# Esta función verifica que se va a desplegar la opción de configuracion general en el sidebar, retorna 1 si se usará y 0 sino.
def verify_configuracion_general_option(estado, rol_id, item_active): 
    if (1 in rol_id and item_active == 1) or (estado != '0' and 2 in rol_id and item_active == 1):
        return 1
    return 0

def verify_datos_basicos_option(estado,rol_id,item_active):
    if(estado == '2' and (1 not in rol_id and 2 not in rol_id) and item_active == 1) or (estado == '4' and (1 not in rol_id and 2 not in rol_id) and item_active ==1):
        return 0
    return 1

def verify_estado_arbitrajes_option(estado,rol_id,item_active):
    return 1


def verify_usuario_option(estado,rol_id, item_active):
    if (1 in rol_id and item_active == 1):
        return 1
    return 0


def verify_asignacion_coordinador_general_option(estado,rol_id,item_active):
    if(1 in rol_id and item_active == 1):
        return 1
    return 0


def verify_asignacion_coordinador_area_option(estado,rol_id,item_active):
    if(estado =='2' and 2 in rol_id and item_active == 1) or (1 in rol_id and item_active == 1):
        return 1
    return 0




def verify_recursos_option(estado,rol_id,item_active):
    if (1 in rol_id and item_active == 1) or (estado =='8' and (2 in rol_id or 3 in rol_id  or 4 in rol_id) and item_active==1):
        return 1
    return 0

def verify_areas_subareas_option(estado,rol_id,item_active):
    if (1 in rol_id and item_active == 1) or (estado == '1' and (2 in rol_id or 3 in rol_id) and item_active == 1) or (estado == '2' and 2 in rol_id and item_active ==1):
        return 1
    return 0


def verify_autores_option(estado,rol_id,item_active):
    if ((estado == '0' or estado =='5' or estado =='6' or estado =='7' or estado =='8') and 1 in rol_id and item_active == 2) or ((estado == '1' or estado =='2' or estado == '3' or estado == '4') and (1 in rol_id or 2 in rol_id) and item_active == 2):
        return 1
    return 0

def verify_arbitros_option(estado,rol_id, item_active):
    if (1 in rol_id and item_active == 2) or (estado == '1' and 2 in rol_id and item_active == 2) or ((estado =='2' or estado == '3' or estado == '4') and (2 in rol_id or 3 in rol_id) and item_active == 2) or (estado =='1' and 3 in rol_id and item_active==2):
        return 1
    return 0

def verify_sesions_arbitraje_option(estado,rol_id, item_active):
    if (1 in rol_id and item_active == 2) or ((estado == '4' or estado =='7') and (2 in rol_id or 3 in rol_id) and item_active == 2):
        return 1
    return 0

def verify_asignar_sesion(estado,rol_id,item_active):
    if(1 in rol_id and item_active == 2) or (estado == '4' and (2 in rol_id or 3 in rol_id) and item_active == 2) or (estado =='7' and 2 in rol_id and item_active == 2):
        return 1
    return 0


def verify_arbitraje_option(estado,rol_id, item_active):
    if (1 in rol_id and item_active == 2) or (estado =='6' and (2 in rol_id) and item_active == 2):
        return 1
    return 0

def verify_trabajo_option(estado, rol_id,item_active):
    if((estado =='3' or estado =='4' or estado =='5')and (2 in rol_id or 3 in rol_id) and item_active == 2) or (1 in rol_id and item_active ==2) or(estado =='6' and 3 in rol_id and item_active ==2):
        return 1
    return 0

def verify_eventos_sidebar_full(estado,rol_id,item_active):
    if (1 in rol_id and item_active == 4):
        return 1
    return 0

def verify_espacio_option(estado,rol_id,item_active):
    if(1 in rol_id and item_active == 4):
        return 1
    return 0

def verify_trabajo_options(estado,rol_id):
    if(estado == '3' and 5 in rol_id):
        return 1
    return 0

# Funciones para verificar los campos del navbar
def verify_configuration(estado,rol_id):
    if ( (estado =='0' and 2 in rol_id) or ((estado != '1' and estado != '8') and 3 in rol_id) or ((estado != '8') and 4 in rol_id) or 5 in rol_id):
        return 0 
    return 1

def verify_arbitration(estado,rol_id):
    if ( ((estado =='0' or estado == '8') and 2 in rol_id) or ((estado == '0' or estado == '8') and 3 in rol_id) or 4 in rol_id or 5 in rol_id):
        return 0 
    return 1

def verify_result(estado,rol_id):
    if ( ((estado !='6' and estado != '7' and estado != '8') and 2 in rol_id) or ((estado != '6' and estado != '8') and 3 in rol_id) or ((estado != '8' and estado != '6') and 4 in rol_id) or (estado != '6' and 5 in rol_id)):
        return 0 
    return 1

def verify_event(estado,rol_id):
    if ( 1 not in rol_id):
        return 0 
    return 1

# def verify_event_app():
#     return 1

def verify_jobs(estado, rol_id):
    if((estado == '3' and 5 in rol_id) or (estado == '5' and 4 in rol_id)):
        return 1
    return 0

def validate_rol_status(estado,rol_id,item_active):
    items={}
    configuracion_general_sidebar = verify_configuracion_general_option(estado, rol_id, item_active)
    usuarios_sidebar = verify_usuario_option(estado,rol_id,item_active)
    recursos_sidebar = verify_recursos_option(estado,rol_id,item_active)
    areas_subareas_sidebar = verify_areas_subareas_option(estado,rol_id,item_active)
    
    autores_sidebar = verify_autores_option(estado,rol_id,item_active)
    arbitros_sidebar = verify_arbitros_option(estado,rol_id,item_active)
    sesion_arbitraje_sidebar = verify_sesions_arbitraje_option(estado,rol_id,item_active)
    arbitraje_sidebar = verify_arbitraje_option(estado,rol_id,item_active)
    eventos_sidebar_full = verify_eventos_sidebar_full(estado,rol_id,item_active)
    asignacion_de_sesion_sidebar = verify_asignar_sesion(estado,rol_id,item_active)

    asignacion_coordinador_general = verify_asignacion_coordinador_general_option(estado,rol_id,item_active)
    asignacion_coordinador_area = verify_asignacion_coordinador_area_option(estado, rol_id,item_active)
    datos_basicos_sidebar = verify_datos_basicos_option(estado,rol_id,item_active)

    trabajos_sidebar = verify_trabajo_option(estado,rol_id,item_active)
    estado_arbitrajes_sidebar = verify_estado_arbitrajes_option(estado,rol_id,item_active)
    espacio_sidebar = verify_espacio_option(estado,rol_id,item_active)

    trabajo_sidebar = verify_trabajo_options(estado,rol_id)

    configuration = verify_configuration(estado,rol_id)
    arbitration = verify_arbitration(estado,rol_id)
    result =  verify_result(estado,rol_id)
    event = verify_event(estado,rol_id)
    jobs = verify_jobs(estado,rol_id)
    #organizer_event = verify_event_app()
    

    # Menu de configuración 
    items.setdefault("configuracion_general_sidebar",[configuracion_general_sidebar,reverse('main_app:data_basic')])
    items.setdefault("usuarios_sidebar",[usuarios_sidebar,reverse('main_app:users_list')])
    items.setdefault("recursos_sidebar",[recursos_sidebar,reverse('recursos:resources_author')])
    items.setdefault("areas_subareas_sidebar",[areas_subareas_sidebar,reverse('arbitrajes:arbitrations_areas_subareas')])
    items.setdefault("estado_arbitrajes_sidebar",[estado_arbitrajes_sidebar,reverse('main_app:arbitration_state')])
    items.setdefault("datos_basicos_sidebar",[datos_basicos_sidebar,reverse('main_app:data_basic')])
    items.setdefault("asignacion_coordinador_general",[asignacion_coordinador_general,reverse('main_app:coord_general')])
    items.setdefault("asignacion_coordinador_area",[asignacion_coordinador_area,reverse('main_app:coord_area')])

    # Menu de arbitraje y seguimiento
    items.setdefault("autores_sidebar",[autores_sidebar,reverse('autores:authors_list')])
    items.setdefault("arbitros_sidebar",[arbitros_sidebar,reverse('arbitrajes:referee_list')])
    items.setdefault("sesion_arbitraje_sidebar",[sesion_arbitraje_sidebar,reverse('sesiones:sesions_list')])
    items.setdefault("arbitraje_sidebar",[arbitraje_sidebar,reverse('arbitrajes:referee_list')])
    items.setdefault("trabajos_sidebar",[trabajos_sidebar,reverse('trabajos:jobs_list')])
    items.setdefault("asignacion_de_sesion_sidebar",[asignacion_de_sesion_sidebar,reverse('arbitrajes:asignacion_de_sesion')])


    # Menu de resultados

    # Menu de eventos 
    items.setdefault("eventos_sidebar_full",[eventos_sidebar_full,reverse('eventos:event_list')])
    items.setdefault("espacio_sidebar",[espacio_sidebar,reverse('sesiones:sesions_space_list')])
    #items.setdefault("verify_event_app",[organizer_event,None])
    
    #Menú de trabajos
    items.setdefault("trabajo_sidebar",[trabajo_sidebar,reverse('trabajos:trabajos')])


    items.setdefault("configuration",[configuration,''])
    items.setdefault("arbitration",[arbitration,''])
    items.setdefault("result",[result,''])
    items.setdefault("event",[event,''])
    items.setdefault("jobs",[jobs,''])

    return items

def get_route_configuracion(estado,rol_id):
    
    if(1 in rol_id or 2 in rol_id):#Caso que sea admin o coordinador general
        return reverse('main_app:data_basic')
    elif 3 in rol_id:
        if(estado == '8'):
            return reverse('recursos:resources_author')
        if(estado == '1'):
            return reverse('arbitrajes:arbitrations_areas_subareas')
    elif 4 in rol_id:
        if(estado == '8'):
            return reverse('recursos:resources_author')


    return None

def get_route_seguimiento(estado,rol_id):
    
    if 1 in rol_id:
        return reverse('autores:authors_list')
    elif 2 in rol_id:
        if(estado == '1' or estado== '2' or estado == '3' or estado == '4'):
            return reverse('autores:authors_list')
        elif(estado == '5'):
            return reverse('trabajos:jobs_list')
        elif(estado == '6'):
            return reverse('arbitrajes:listado')
        elif(estado == '7'):
            return reverse('arbitrajes:asignacion_de_sesion')
    elif 3 in rol_id:
        if(estado =='1' or estado == '2' or estado == '3' or estado == '4'):
            return reverse('arbitrajes:referee_list')
        elif(estado =='5' or estado == '6'):
            return reverse('trabajos:jobs_list')
        elif(estado == '7'):
            return reverse('sesiones:sesions_list')
#Obtener roles del usuario
def get_roles(user_id):
    rol = Usuario_asovac.objects.get(usuario_id=user_id).rol.all()

    rol_id=[]
    for item in rol:
        rol_id.append(item.id)

    return rol_id

def get_route_trabajos_sidebar(estado,rol_id,item_active):
    if (estado =='4' and 2 in rol_id and item_active == 2):
        return reverse('trabajos:trabajos_evaluados')
    else:
        return reverse('trabajos:jobs_list')


def get_route_trabajos_navbar(estado,rol_id):
    if(estado =='3' and 5 in rol_id):
        return reverse('trabajos:trabajos')
    if(estado =='5' and 4 in rol_id):
        return reverse('trabajos:trabajos_evaluados')
    return None 

def get_route_resultados(estado,rol_id):
    if(estado=='6' and 5 in rol_id):
        return reverse('trabajos:trabajos_resultados_autor')
    else:
        return reverse('main_app:total')


#Update state of arbitration
def update_state_arbitration(arbitraje_id,estado):
    new_state = Sistema_asovac.objects.get(pk=arbitraje_id)
    #update Sistema_asovac
    new_state.estado_arbitraje = estado
    # save in DB
    new_state.save()
    return estado


#################################################
######### VIEWS BACKEND #########################
#################################################

# Create your views here.
def login(request):
    form = MyLoginForm()
    context = {
        'nombre_vista' : 'Login',
        'form' : form,
    }
    return render(request, 'main_app_login.html', context)

def home(request):
    # queryset
    arbitraje_data = Sistema_asovac.objects.all()
    secondary_navbar_options = ['Bienvenido']

    rol_id=get_roles(request.user.id)
    # print(arbitraje_data)
    context = {
        'nombre_vista' : 'Home',
        'secondary_navbar_options' : secondary_navbar_options,
        'arb_data' : arbitraje_data,
        'rol_id' : rol_id,
    }
    return render(request, 'main_app_home.html', context)

def create_arbitraje(request):
    form = CreateArbitrajeForm()
    context = {
                    'nombre_vista' : 'Crear Arbitraje',
                    'username' : request.user.username,
                    'form' : form,
                }
    if request.method == 'POST':
        form = CreateArbitrajeForm(request.POST or None)
        if form.is_valid():
            form.save()
            # print(form)
            arbitraje_data = Sistema_asovac.objects.all()
            context = {        
                'username' : request.user.username,
                'form' : form,
                'arb_data': arbitraje_data,
                }
            return redirect('main_app:home')        
    return render(request, 'main_app_create_arbitraje.html', context)

def email_test(request):
    context = {
        'nombre_vista' : 'Email-Test',
        'username' : 'Rabindranath Ferreira',
        'resumen_title': 'Escalamiento a escala industrial de una crema azufrada optimizada mediante un diseño erandom_passwordperimental',
        'authors': ['Karla Calo', 'Luis Henríquez']
    }
    return render(request, 'resumen_rejected_email.html', context)

def listado_trabajos(request):
    context = {
        'nombre_vista' : 'Lista de Trabajos',
        'username' : 'Rabindranath Ferreira',
    }
    return render(request, 'main_app_resumenes_trabajos_list.html', context)

def detalles_resumen(request):
    context = {
        'nombre_vista' : 'Detalles de Resumen',
        'username' : 'Rabindranath Ferreira',
    }
    return render(request, 'main_app_detalle_resumen.html', context)


def dashboard(request):
    main_navbar_options = [{'title':'Configuración',   'icon': 'fa-cogs',      'active': True},
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': False},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]
    
    secondary_navbar_options = ['']

    if request.POST:
        request.session['estado'] = request.POST['estado']
        request.session['arbitraje_id'] = request.POST['arbitraje_id']
    else:
        estado=-1
        arbitraje_id=-1

    
    rol_id=get_roles(request.user.id)
    
    
    estado = request.session['estado']
    arbitraje_id = request.session['arbitraje_id']

    item_active = 1
    #print(request.session['estado'])
    items=validate_rol_status(estado,rol_id,item_active)

    route_conf= get_route_configuracion(estado,rol_id)
    route_seg= get_route_seguimiento(estado,rol_id)
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)
    route_trabajos_navbar = get_route_trabajos_navbar(estado,rol_id)
    route_resultados = get_route_resultados(estado,rol_id)
    # print items

    # for item,val in items.items():
        # print item, ":", val[0]

    context = {
        'nombre_vista' : 'Dashboard',
        'main_navbar_options' : main_navbar_options,
        'secondary_navbar_options' : secondary_navbar_options,
        'estado' : estado,
        #'rol' : rol,
        'rol_id' : rol_id,
        'arbitraje_id' : arbitraje_id,
        'item_active' : item_active,
        'items':items,
        'configuracion_general_sidebar': items["configuracion_general_sidebar"][0],
        'usuarios_sidebar' : items["usuarios_sidebar"][0],
        'recursos_sidebar' : items["recursos_sidebar"][0],
        'areas_subareas_sidebar' : items["areas_subareas_sidebar"][0],
        'autores_sidebar' : items["autores_sidebar"][0],
        'arbitros_sidebar' : items["arbitros_sidebar"][0],
        'sesion_arbitraje_sidebar' : items["sesion_arbitraje_sidebar"][0],
        'arbitraje_sidebar' : items["arbitraje_sidebar"][0],
        'eventos_sidebar_full' : items["eventos_sidebar_full"][0],
        'asignacion_coordinador_general': items["asignacion_coordinador_general"][0],
        'asignacion_coordinador_area': items["asignacion_coordinador_area"][0],
        'datos_basicos_sidebar' : items["datos_basicos_sidebar"][0],
        'trabajos_sidebar':items["trabajos_sidebar"][0],
        'estado_arbitrajes_sidebar':items["estado_arbitrajes_sidebar"][0],
        'espacio_sidebar':items["espacio_sidebar"][0],
        'asignacion_de_sesion_sidebar':items["asignacion_de_sesion_sidebar"][0],
        'trabajo_sidebar': items["trabajo_sidebar"][0],
        'verify_configuration':items["configuration"][0],
        'verify_arbitration':items["arbitration"][0],
        'verify_result':items["result"][0],
        'verify_event':items["event"][0],
        'verify_jobs':items["jobs"][0],
        'route_conf':route_conf,
        'route_seg':route_seg,
        'route_trabajos_sidebar':route_trabajos_sidebar,
        'route_trabajos_navbar': route_trabajos_navbar,
        'route_resultados': route_resultados,
    }
    return render(request, 'main_app_dashboard.html', context)

def data_basic(request):
    form= DataBasicForm()

    main_navbar_options = [{'title':'Configuración','icon': 'fa-cogs','active': True },
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': False},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    secondary_navbar_options = ['']
    
    rol_id=get_roles(request.user.id)

    # print (rol_id)
    
    estado = request.session['estado']
    arbitraje_id = request.session['arbitraje_id']
    
    arbitraje = Sistema_asovac.objects.get(id = arbitraje_id)

    if request.POST:
        opcion = request.POST['generar_clave']
        random_password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
            
        if opcion == '1': #Caso de generar clave  para coordinador general
            random_password += 'COG'
            arbitraje.clave_maestra_coordinador_general = random_password
            arbitraje.save()
            messages.success(request, 'La contraseña de coordinador general ha sido generada.')

            usuarios = Usuario_asovac.objects.filter(Sistema_asovac_id = arbitraje.id, rol = 2) | Usuario_asovac.objects.filter(Sistema_asovac_id = arbitraje.id, rol = 1) 
            nombre_sistema = Sistema_asovac.objects.get(id=request.session['arbitraje_id']).nombre
            nombre_rol = Rol.objects.get(id=2).nombre
            context = {
            'rol': nombre_rol,
            'sistema': nombre_sistema,
            'password': random_password,
            }
            msg_plain = render_to_string('../templates/email_templates/password_generator.txt', context)
            msg_html = render_to_string('../templates/email_templates/password_generator.html', context)
            
            for item in usuarios:
                
                send_mail(
                        'Asignación de contraseña',         #titulo
                        msg_plain,                          #mensaje txt
                        config('EMAIL_HOST_USER'),          #email de envio
                        [item.usuario.email],               #destinatario
                        html_message=msg_html,              #mensaje en html
                        )

        
        elif opcion == '2':#Caso de generar clave para coordinador de area
            random_password+= 'COA'
            arbitraje.clave_maestra_coordinador_area = random_password
            arbitraje.save()
            messages.success(request, 'La contraseña de coordinador de area ha sido generada.')

            usuarios = Usuario_asovac.objects.filter(Sistema_asovac_id = arbitraje.id, rol = 3) | Usuario_asovac.objects.filter(Sistema_asovac_id = arbitraje.id, rol = 1) 
            nombre_sistema = Sistema_asovac.objects.get(id=request.session['arbitraje_id']).nombre
            nombre_rol = Rol.objects.get(id=3).nombre
            context = {
            'rol': nombre_rol,
            'sistema': nombre_sistema,
            'password': random_password,
            }
            msg_plain = render_to_string('../templates/email_templates/password_generator.txt', context)
            msg_html = render_to_string('../templates/email_templates/password_generator.html', context)
            
            for item in usuarios:
                
                send_mail(
                        'Asignación de contraseña',         #titulo
                        msg_plain,                          #mensaje txt
                        config('EMAIL_HOST_USER'),          #email de envio
                        [item.usuario.email],               #destinatario
                        html_message=msg_html,              #mensaje en html
                        )
        

        elif opcion == '3':#Caso de generar clave para arbitro de subarea
            random_password += 'ARS'
            arbitraje.clave_maestra_arbitro_subarea = random_password
            arbitraje.save()
            messages.success(request, 'La contraseña de arbitro de subarea ha sido generada.')

            usuarios = Usuario_asovac.objects.filter(Sistema_asovac_id = arbitraje.id, rol = 4) | Usuario_asovac.objects.filter(Sistema_asovac_id = arbitraje.id, rol = 1) 
            nombre_sistema = Sistema_asovac.objects.get(id=request.session['arbitraje_id']).nombre
            nombre_rol = Rol.objects.get(id=4).nombre
            context = {
            'rol': nombre_rol,
            'sistema': nombre_sistema,
            'password': random_password,
            }
            msg_plain = render_to_string('../templates/email_templates/password_generator.txt', context)
            msg_html = render_to_string('../templates/email_templates/password_generator.html', context)
            
            for item in usuarios:
                
                send_mail(
                        'Asignación de contraseña',         #titulo
                        msg_plain,                          #mensaje txt
                        config('EMAIL_HOST_USER'),          #email de envio
                        [item.usuario.email],               #destinatario
                        html_message=msg_html,              #mensaje en html
                        )
        

        print("The password is:"+random_password)



    item_active = 1
    items=validate_rol_status(estado,rol_id,item_active)
   
    route_conf= get_route_configuracion(estado,rol_id)
    route_seg= get_route_seguimiento(estado,rol_id)
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)
    route_trabajos_navbar = get_route_trabajos_navbar(estado,rol_id)
    route_resultados = get_route_resultados(estado,rol_id)

    # print items


    context = {
        'nombre_vista' : 'Configuracion general',
        'main_navbar_options' : main_navbar_options,
        'secondary_navbar_options' : secondary_navbar_options,
        'estado' : estado,
        #'rol' : rol,
        'rol_id' : rol_id,
        'arbitraje_id' : arbitraje_id,
        'arbitraje':arbitraje,
        'item_active' : item_active,
        'items':items,
        'configuracion_general_sidebar': items["configuracion_general_sidebar"][0],
        'usuarios_sidebar' : items["usuarios_sidebar"][0],
        'recursos_sidebar' : items["recursos_sidebar"][0],
        'areas_subareas_sidebar' : items["areas_subareas_sidebar"][0],
        'autores_sidebar' : items["autores_sidebar"][0],
        'arbitros_sidebar' : items["arbitros_sidebar"][0],
        'sesion_arbitraje_sidebar' : items["sesion_arbitraje_sidebar"][0],
        'arbitraje_sidebar' : items["arbitraje_sidebar"][0],
        'eventos_sidebar_full' : items["eventos_sidebar_full"][0],
        'asignacion_coordinador_general': items["asignacion_coordinador_general"][0],
        'asignacion_coordinador_area': items["asignacion_coordinador_area"][0],
        'datos_basicos_sidebar' : items["datos_basicos_sidebar"][0],
        'trabajos_sidebar':items["trabajos_sidebar"][0],
        'estado_arbitrajes_sidebar':items["estado_arbitrajes_sidebar"][0],
        'espacio_sidebar':items["espacio_sidebar"][0],
        'asignacion_de_sesion_sidebar':items["asignacion_de_sesion_sidebar"][0],
        'trabajo_sidebar': items["trabajo_sidebar"][0],
        'verify_configuration':items["configuration"][0],
        'verify_arbitration':items["arbitration"][0],
        'verify_result':items["result"][0],
        'verify_event':items["event"][0],
        'verify_jobs':items["jobs"][0],
        'route_conf':route_conf,
        'route_seg':route_seg,
        'route_trabajos_sidebar':route_trabajos_sidebar,
        'route_trabajos_navbar': route_trabajos_navbar,
        'route_resultados': route_resultados,
    }
    return render(request, 'main_app_data_basic.html', context)

def state_arbitration(request):
    main_navbar_options = [{'title':'Configuración',   'icon': 'fa-cogs',      'active': True},
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': False},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    secondary_navbar_options = ['']

    rol_id=get_roles(request.user.id)

    # print (rol_id)
    estado = request.session['estado']
    arbitraje_id = request.session['arbitraje_id']
    user_id = request.user.id

    item_active = 1
    items=validate_rol_status(estado,rol_id,item_active)

    route_conf= get_route_configuracion(estado,rol_id)
    route_seg= get_route_seguimiento(estado,rol_id)
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)
    route_trabajos_navbar = get_route_trabajos_navbar(estado,rol_id)
    route_resultados = get_route_resultados(estado,rol_id)

    # si se envia el cambio de estado via post se actualiza en bd
    if request.method == 'POST':
        estado = request.POST['estado']
        #print(estado)
        request.session['estado'] = update_state_arbitration(arbitraje_id,estado)

    # si entro en el post se actualiza el estado de lo contrario no cambia y se lo paso a la vista igualmente        
    estado = request.session['estado']
    context = {
        'nombre_vista' : 'Configuracion general',
        'main_navbar_options' : main_navbar_options,
        'secondary_navbar_options' : secondary_navbar_options,
        'estado' : estado,
        #'rol' : rol,
        'rol_id' : rol_id,
        'arbitraje_id' : arbitraje_id,
        'item_active' : item_active,
        'items':items,
        'configuracion_general_sidebar': items["configuracion_general_sidebar"][0],
        'usuarios_sidebar' : items["usuarios_sidebar"][0],
        'recursos_sidebar' : items["recursos_sidebar"][0],
        'areas_subareas_sidebar' : items["areas_subareas_sidebar"][0],
        'autores_sidebar' : items["autores_sidebar"][0],
        'arbitros_sidebar' : items["arbitros_sidebar"][0],
        'sesion_arbitraje_sidebar' : items["sesion_arbitraje_sidebar"][0],
        'arbitraje_sidebar' : items["arbitraje_sidebar"][0],
        'eventos_sidebar_full' : items["eventos_sidebar_full"][0],
        'asignacion_coordinador_general': items["asignacion_coordinador_general"][0],
        'asignacion_coordinador_area': items["asignacion_coordinador_area"][0],
        'datos_basicos_sidebar' : items["datos_basicos_sidebar"][0],
        'trabajos_sidebar':items["trabajos_sidebar"][0],
        'estado_arbitrajes_sidebar':items["estado_arbitrajes_sidebar"][0],
        'espacio_sidebar':items["espacio_sidebar"][0],
        'asignacion_de_sesion_sidebar':items["asignacion_de_sesion_sidebar"][0],
        'trabajo_sidebar': items["trabajo_sidebar"][0],
        'verify_configuration':items["configuration"][0],
        'verify_arbitration':items["arbitration"][0],
        'verify_result':items["result"][0],
        'verify_event':items["event"][0],
        'verify_jobs':items["jobs"][0],
        'route_conf':route_conf,
        'route_seg':route_seg,
        'route_trabajos_sidebar':route_trabajos_sidebar,
        'route_trabajos_navbar': route_trabajos_navbar,
        'route_resultados': route_resultados,
    }
    return render(request, 'main_app_status_arbitration.html', context)

def users_list(request):

    main_navbar_options = [{'title':'Configuración',   'icon': 'fa-cogs',      'active': True},
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': False},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    secondary_navbar_options = ['']

    rol_id=get_roles(request.user.id)

    # print (rol_id)
    estado = request.session['estado']
    arbitraje_id = request.session['arbitraje_id']

    item_active = 1
    items=validate_rol_status(estado,rol_id,item_active)

    route_conf= get_route_configuracion(estado,rol_id)
    route_seg= get_route_seguimiento(estado,rol_id)
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)
    route_trabajos_navbar = get_route_trabajos_navbar(estado,rol_id)
    route_resultados = get_route_resultados(estado,rol_id)

    # print items

    context = {
        'nombre_vista' : 'Usuarios',
        'main_navbar_options' : main_navbar_options,
        'secondary_navbar_options' : secondary_navbar_options,
        'estado' : estado,
        #'rol' : rol,
        'rol_id' : rol_id,
        'arbitraje_id' : arbitraje_id,
        'item_active' : item_active,
        'items':items,
        'configuracion_general_sidebar': items["configuracion_general_sidebar"][0],
        'usuarios_sidebar' : items["usuarios_sidebar"][0],
        'recursos_sidebar' : items["recursos_sidebar"][0],
        'areas_subareas_sidebar' : items["areas_subareas_sidebar"][0],
        'autores_sidebar' : items["autores_sidebar"][0],
        'arbitros_sidebar' : items["arbitros_sidebar"][0],
        'sesion_arbitraje_sidebar' : items["sesion_arbitraje_sidebar"][0],
        'arbitraje_sidebar' : items["arbitraje_sidebar"][0],
        'eventos_sidebar_full' : items["eventos_sidebar_full"][0],
        'asignacion_coordinador_general': items["asignacion_coordinador_general"][0],
        'asignacion_coordinador_area': items["asignacion_coordinador_area"][0],
        'datos_basicos_sidebar' : items["datos_basicos_sidebar"][0],
        'trabajos_sidebar':items["trabajos_sidebar"][0],
        'estado_arbitrajes_sidebar':items["estado_arbitrajes_sidebar"][0],
        'espacio_sidebar':items["espacio_sidebar"][0],
        'asignacion_de_sesion_sidebar':items["asignacion_de_sesion_sidebar"][0],
        'trabajo_sidebar': items["trabajo_sidebar"][0],
        'verify_configuration':items["configuration"][0],
        'verify_arbitration':items["arbitration"][0],
        'verify_result':items["result"][0],
        'verify_event':items["event"][0],
        'verify_jobs':items["jobs"][0],
        'route_conf':route_conf,
        'route_seg':route_seg,
        'route_trabajos_sidebar':route_trabajos_sidebar,
        'route_trabajos_navbar': route_trabajos_navbar,
        'route_resultados': route_resultados,
    }
    return render(request, 'main_app_users_list.html', context)
    
def register(request):
    if request.method == 'POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha registrado de manera erandom_passworditosa.')
            context={"form":form,}
            return redirect('login')

        else:
            context={"form":form,}
            return render(request,'main_app_register.html',context)
            
    else:
        form = RegisterForm()
        context={"form":form,}
        return render(request,'main_app_register.html',context)

def user_edit(request):
    main_navbar_options = [{'title':'Configuración',   'icon': 'fa-cogs',      'active': True},
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': False},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    secondary_navbar_options = ['']

    rol_id=get_roles(request.user.id)

    # print (rol_id)
    estado = request.session['estado']
    arbitraje_id = request.session['arbitraje_id']

    item_active = 1
    items=validate_rol_status(estado,rol_id,item_active)

    route_conf= get_route_configuracion(estado,rol_id)
    route_seg= get_route_seguimiento(estado,rol_id)
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)
    route_trabajos_navbar = get_route_trabajos_navbar(estado,rol_id)
    route_resultados = get_route_resultados(estado,rol_id)
    # print items

    context = {
        'nombre_vista' : 'Usuarios',
        'main_navbar_options' : main_navbar_options,
        'secondary_navbar_options' : secondary_navbar_options,
        'estado' : estado,
        #'rol' : rol,
        'rol_id' : rol_id,
        'arbitraje_id' : arbitraje_id,
        'item_active' : item_active,
        'items':items,
        'configuracion_general_sidebar': items["configuracion_general_sidebar"][0],
        'usuarios_sidebar' : items["usuarios_sidebar"][0],
        'recursos_sidebar' : items["recursos_sidebar"][0],
        'areas_subareas_sidebar' : items["areas_subareas_sidebar"][0],
        'autores_sidebar' : items["autores_sidebar"][0],
        'arbitros_sidebar' : items["arbitros_sidebar"][0],
        'sesion_arbitraje_sidebar' : items["sesion_arbitraje_sidebar"][0],
        'arbitraje_sidebar' : items["arbitraje_sidebar"][0],
        'eventos_sidebar_full' : items["eventos_sidebar_full"][0],
        'asignacion_coordinador_general': items["asignacion_coordinador_general"][0],
        'asignacion_coordinador_area': items["asignacion_coordinador_area"][0],
        'datos_basicos_sidebar' : items["datos_basicos_sidebar"][0],
        'trabajos_sidebar':items["trabajos_sidebar"][0],
        'estado_arbitrajes_sidebar':items["estado_arbitrajes_sidebar"][0],
        'espacio_sidebar':items["espacio_sidebar"][0],
        'asignacion_de_sesion_sidebar':items["asignacion_de_sesion_sidebar"][0],
        'trabajo_sidebar': items["trabajo_sidebar"][0],
        'verify_configuration':items["configuration"][0],
        'verify_arbitration':items["arbitration"][0],
        'verify_result':items["result"][0],
        'verify_event':items["event"][0],
        'verify_jobs':items["jobs"][0],
        'route_conf':route_conf,
        'route_seg':route_seg,
        'route_trabajos_sidebar':route_trabajos_sidebar,
        'route_trabajos_navbar': route_trabajos_navbar,
        'route_resultados': route_resultados,
    }
    return render(request, 'main_app_edit_user.html', context)

def user_roles(request):
    main_navbar_options = [{'title':'Configuración',   'icon': 'fa-cogs',      'active': True},
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': False},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    secondary_navbar_options = ['']

    rol_id=get_roles(request.user.id)

    # print (rol_id)
    estado = request.session['estado']
    arbitraje_id = request.session['arbitraje_id']

    item_active = 1
    items=validate_rol_status(estado,rol_id,item_active)

    route_conf= get_route_configuracion(estado,rol_id)
    route_seg= get_route_seguimiento(estado,rol_id)
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)
    route_trabajos_navbar = get_route_trabajos_navbar(estado,rol_id)
    route_resultados = get_route_resultados(estado,rol_id)

    # print items

    context = {
        'nombre_vista' : 'Usuarios',
        'main_navbar_options' : main_navbar_options,
        'secondary_navbar_options' : secondary_navbar_options,
        'estado' : estado,
        #'rol' : rol,
        'rol_id' : rol_id,
        'arbitraje_id' : arbitraje_id,
        'item_active' : item_active,
        'items':items,
        'configuracion_general_sidebar': items["configuracion_general_sidebar"][0],
        'usuarios_sidebar' : items["usuarios_sidebar"][0],
        'recursos_sidebar' : items["recursos_sidebar"][0],
        'areas_subareas_sidebar' : items["areas_subareas_sidebar"][0],
        'autores_sidebar' : items["autores_sidebar"][0],
        'arbitros_sidebar' : items["arbitros_sidebar"][0],
        'sesion_arbitraje_sidebar' : items["sesion_arbitraje_sidebar"][0],
        'arbitraje_sidebar' : items["arbitraje_sidebar"][0],
        'eventos_sidebar_full' : items["eventos_sidebar_full"][0],
        'asignacion_coordinador_general': items["asignacion_coordinador_general"][0],
        'asignacion_coordinador_area': items["asignacion_coordinador_area"][0],
        'datos_basicos_sidebar' : items["datos_basicos_sidebar"][0],
        'trabajos_sidebar':items["trabajos_sidebar"][0],
        'estado_arbitrajes_sidebar':items["estado_arbitrajes_sidebar"][0],
        'espacio_sidebar':items["espacio_sidebar"][0],
        'asignacion_de_sesion_sidebar':items["asignacion_de_sesion_sidebar"][0],
        'trabajo_sidebar': items["trabajo_sidebar"][0],
        'verify_configuration':items["configuration"][0],
        'verify_arbitration':items["arbitration"][0],
        'verify_result':items["result"][0],
        'verify_event':items["event"][0],
        'verify_jobs':items["jobs"][0],
        'route_conf':route_conf,
        'route_seg':route_seg,
        'route_trabajos_sidebar':route_trabajos_sidebar,
        'route_trabajos_navbar': route_trabajos_navbar,
        'route_resultados': route_resultados,
    }
    return render(request, 'main_app_user_roles.html', context)

def coord_general(request):
    main_navbar_options = [{'title':'Configuración',   'icon': 'fa-cogs',      'active': True},
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': False},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    secondary_navbar_options = ['']

    rol_id=get_roles(request.user.id)

    # print (rol_id)
    estado = request.session['estado']
    arbitraje_id = request.session['arbitraje_id']

    item_active = 1
    items=validate_rol_status(estado,rol_id,item_active)

    route_conf= get_route_configuracion(estado,rol_id)
    route_seg= get_route_seguimiento(estado,rol_id)
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)
    route_trabajos_navbar = get_route_trabajos_navbar(estado,rol_id)
    route_resultados = get_route_resultados(estado,rol_id)

    # print items

    context = {
        'nombre_vista' : 'Usuarios',
        'main_navbar_options' : main_navbar_options,
        'secondary_navbar_options' : secondary_navbar_options,
        'estado' : estado,
        #'rol' : rol,
        'rol_id' : rol_id,
        'arbitraje_id' : arbitraje_id,
        'item_active' : item_active,
        'items':items,
        'configuracion_general_sidebar': items["configuracion_general_sidebar"][0],
        'usuarios_sidebar' : items["usuarios_sidebar"][0],
        'recursos_sidebar' : items["recursos_sidebar"][0],
        'areas_subareas_sidebar' : items["areas_subareas_sidebar"][0],
        'autores_sidebar' : items["autores_sidebar"][0],
        'arbitros_sidebar' : items["arbitros_sidebar"][0],
        'sesion_arbitraje_sidebar' : items["sesion_arbitraje_sidebar"][0],
        'arbitraje_sidebar' : items["arbitraje_sidebar"][0],
        'eventos_sidebar_full' : items["eventos_sidebar_full"][0],
        'asignacion_coordinador_general': items["asignacion_coordinador_general"][0],
        'asignacion_coordinador_area': items["asignacion_coordinador_area"][0],
        'datos_basicos_sidebar' : items["datos_basicos_sidebar"][0],
        'trabajos_sidebar':items["trabajos_sidebar"][0],
        'estado_arbitrajes_sidebar':items["estado_arbitrajes_sidebar"][0],
        'espacio_sidebar':items["espacio_sidebar"][0],
        'asignacion_de_sesion_sidebar':items["asignacion_de_sesion_sidebar"][0],
        'trabajo_sidebar': items["trabajo_sidebar"][0],
        'verify_configuration':items["configuration"][0],
        'verify_arbitration':items["arbitration"][0],
        'verify_result':items["result"][0],
        'verify_event':items["event"][0],
        'verify_jobs':items["jobs"][0],
        'route_conf':route_conf,
        'route_seg':route_seg,
        'route_trabajos_sidebar':route_trabajos_sidebar,
        'route_trabajos_navbar': route_trabajos_navbar,
        'route_resultados': route_resultados,
    }
    return render(request, 'main_app_coord_general.html', context)

def coord_area(request):
    main_navbar_options = [{'title':'Configuración',   'icon': 'fa-cogs',      'active': True},
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': False},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    secondary_navbar_options = ['']

    rol_id=get_roles(request.user.id)

    # print (rol_id)
    estado = request.session['estado']
    arbitraje_id = request.session['arbitraje_id']

    item_active = 1
    items=validate_rol_status(estado,rol_id,item_active)

    route_conf= get_route_configuracion(estado,rol_id)
    route_seg= get_route_seguimiento(estado,rol_id)
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)
    route_trabajos_navbar = get_route_trabajos_navbar(estado,rol_id)
    route_resultados = get_route_resultados(estado,rol_id)
    
    # print items

    context = {
        'nombre_vista' : 'Usuarios',
        'main_navbar_options' : main_navbar_options,
        'secondary_navbar_options' : secondary_navbar_options,
        'estado' : estado,
        #'rol' : rol,
        'rol_id' : rol_id,
        'arbitraje_id' : arbitraje_id,
        'item_active' : item_active,
        'items':items,
        'configuracion_general_sidebar': items["configuracion_general_sidebar"][0],
        'usuarios_sidebar' : items["usuarios_sidebar"][0],
        'recursos_sidebar' : items["recursos_sidebar"][0],
        'areas_subareas_sidebar' : items["areas_subareas_sidebar"][0],
        'autores_sidebar' : items["autores_sidebar"][0],
        'arbitros_sidebar' : items["arbitros_sidebar"][0],
        'sesion_arbitraje_sidebar' : items["sesion_arbitraje_sidebar"][0],
        'arbitraje_sidebar' : items["arbitraje_sidebar"][0],
        'eventos_sidebar_full' : items["eventos_sidebar_full"][0],
        'asignacion_coordinador_general': items["asignacion_coordinador_general"][0],
        'asignacion_coordinador_area': items["asignacion_coordinador_area"][0],
        'datos_basicos_sidebar' : items["datos_basicos_sidebar"][0],
        'trabajos_sidebar':items["trabajos_sidebar"][0],
        'estado_arbitrajes_sidebar':items["estado_arbitrajes_sidebar"][0],
        'espacio_sidebar':items["espacio_sidebar"][0],
        'asignacion_de_sesion_sidebar':items["asignacion_de_sesion_sidebar"][0],
        'trabajo_sidebar': items["trabajo_sidebar"][0],
        'verify_configuration':items["configuration"][0],
        'verify_arbitration':items["arbitration"][0],
        'verify_result':items["result"][0],
        'verify_event':items["event"][0],
        'verify_jobs':items["jobs"][0],
        'route_conf':route_conf,
        'route_seg':route_seg,
        'route_trabajos_sidebar':route_trabajos_sidebar,
        'route_trabajos_navbar': route_trabajos_navbar,
        'route_resultados': route_resultados,
    }
    return render(request, 'main_app_coord_area.html', context)

def total(request):
    main_navbar_options = [{'title':'Configuración',   'icon': 'fa-cogs',      'active': False},
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': False},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': True},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    secondary_navbar_options = ['']

    rol_id=get_roles(request.user.id)

    # print (rol_id)
    estado = request.session['estado']
    arbitraje_id = request.session['arbitraje_id']
    
    item_active = 3
    items=validate_rol_status(estado,rol_id,item_active)

    route_conf= get_route_configuracion(estado,rol_id)
    route_seg= get_route_seguimiento(estado,rol_id)
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)
    route_trabajos_navbar = get_route_trabajos_navbar(estado,rol_id)
    route_resultados = get_route_resultados(estado,rol_id)

    # print items

    context = {
        'nombre_vista' : 'Usuarios',
        'main_navbar_options' : main_navbar_options,
        'secondary_navbar_options' : secondary_navbar_options,
        'estado' : estado,
        #'rol' : rol,
        'rol_id' : rol_id,
        'arbitraje_id' : arbitraje_id,
        'item_active' : item_active,
        'items':items,
        'configuracion_general_sidebar': items["configuracion_general_sidebar"][0],
        'usuarios_sidebar' : items["usuarios_sidebar"][0],
        'recursos_sidebar' : items["recursos_sidebar"][0],
        'areas_subareas_sidebar' : items["areas_subareas_sidebar"][0],
        'autores_sidebar' : items["autores_sidebar"][0],
        'arbitros_sidebar' : items["arbitros_sidebar"][0],
        'sesion_arbitraje_sidebar' : items["sesion_arbitraje_sidebar"][0],
        'arbitraje_sidebar' : items["arbitraje_sidebar"][0],
        'eventos_sidebar_full' : items["eventos_sidebar_full"][0],
        'asignacion_coordinador_general': items["asignacion_coordinador_general"][0],
        'asignacion_coordinador_area': items["asignacion_coordinador_area"][0],
        'datos_basicos_sidebar' : items["datos_basicos_sidebar"][0],
        'trabajos_sidebar':items["trabajos_sidebar"][0],
        'estado_arbitrajes_sidebar':items["estado_arbitrajes_sidebar"][0],
        'espacio_sidebar':items["espacio_sidebar"][0],
        'asignacion_de_sesion_sidebar':items["asignacion_de_sesion_sidebar"][0],
        'trabajo_sidebar': items["trabajo_sidebar"][0],
        'verify_configuration':items["configuration"][0],
        'verify_arbitration':items["arbitration"][0],
        'verify_result':items["result"][0],
        'verify_event':items["event"][0],
        'verify_jobs':items["jobs"][0],
        'route_conf':route_conf,
        'route_seg':route_seg,
        'route_trabajos_sidebar':route_trabajos_sidebar,
        'route_trabajos_navbar': route_trabajos_navbar,
        'route_resultados': route_resultados,
    }
    return render(request, 'main_app_totales.html', context)

def apps_selection(request):
    # queryset
    # arbitraje_data = Sistema_asovac.objects.all()

    # if request.method == 'POST':
    #     context = {
    #         'nombre_vista' : 'Home',
    #         'arb_data' : arbitraje_data,
    #     }
    #     return render(request, 'main_app_home.html',context)
    context = {
    
    }
    return render(request, 'main_app_aplicaciones_opc.html',context)