# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#import settings
from django.conf import settings
# import para envio de correo
from django.core.mail import send_mail
from main_app.models import Rol,Sistema_asovac,Usuario_asovac
from main_app.views import verify_crear_trabajo_option, get_route_trabajos_sidebar, verify_asignar_sesion, get_roles, verify_configuration, verify_arbitration,verify_result,verify_event,validate_rol_status,verify_configuracion_general_option,verify_datos_basicos_option,verify_estado_arbitrajes_option,verify_usuario_option,verify_asignacion_coordinador_general_option,verify_asignacion_coordinador_area_option,verify_recursos_option,verify_areas_subareas_option,verify_autores_option,verify_arbitros_option,verify_sesions_arbitraje_option,verify_arbitraje_option,verify_trabajo_option,verify_eventos_sidebar_full,verify_espacio_option,validate_rol_status,get_route_configuracion,get_route_seguimiento, verify_jobs

# Create your views here.
def sesiones_pag(request):
    context = {
        "nombre_vista": 'sesiones'
    }
    return render(request,"test_views.html",context)

def sesions_list(request):
    main_navbar_options = [{'title':'Configuración',   'icon': 'fa-cogs',      'active': False},
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': True},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    secondary_navbar_options = ['']

    rol_id=get_roles(request.user.id)


    estado = request.session['estado']
    event_id = request.session['arbitraje_id']

    item_active = 2
    items=validate_rol_status(estado,rol_id,item_active)

    route_conf= get_route_configuracion(validate_rol_status(estado,rol_id,1))
    route_seg= get_route_seguimiento(validate_rol_status(estado,rol_id,2))
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)
    
    # print items

    context = {
        'nombre_vista' : 'Recursos',
        'main_navbar_options' : main_navbar_options,
        'secondary_navbar_options' : secondary_navbar_options,
        'estado' : estado,
        #'rol' : rol,
        'rol_id' : rol_id,
        'event_id' : event_id,
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
        'crear_trabajo_sidebar': items["crear_trabajo_sidebar"][0],
        'verify_configuration':items["configuration"][0],
        'verify_arbitration':items["arbitration"][0],
        'verify_result':items["result"][0],
        'verify_event':items["event"][0],
        'verify_jobs':items["jobs"][0],
        'route_conf':route_conf,
        'route_seg':route_seg,
        'route_trabajos_sidebar':route_trabajos_sidebar,
    }
    return render(request, 'sesiones_sesions_list.html', context)

def sesions_edit(request):
    main_navbar_options = [{'title':'Configuración',   'icon': 'fa-cogs',      'active': False},
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': True},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    secondary_navbar_options = ['']

    rol_id=get_roles(request.user.id)

    estado = request.session['estado']
    event_id = request.session['arbitraje_id']

    item_active = 2
    items=validate_rol_status(estado,rol_id,item_active)

    route_conf= get_route_configuracion(validate_rol_status(estado,rol_id,1))
    route_seg= get_route_seguimiento(validate_rol_status(estado,rol_id,2))
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)

    # print items

    context = {
        'nombre_vista' : 'Recursos',
        'main_navbar_options' : main_navbar_options,
        'secondary_navbar_options' : secondary_navbar_options,
        'estado' : estado,
        #'rol' : rol,
        'rol_id' : rol_id,
        'event_id' : event_id,
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
        'crear_trabajo_sidebar': items["crear_trabajo_sidebar"][0],
        'verify_configuration':items["configuration"][0],
        'verify_arbitration':items["arbitration"][0],
        'verify_result':items["result"][0],
        'verify_event':items["event"][0],
        'verify_jobs':items["jobs"][0],
        'route_conf':route_conf,
        'route_seg':route_seg,
    }
    return render(request, 'sesiones_sesions_edit.html', context)

def sesions_space_list(request):
    main_navbar_options = [{'title':'Configuración',   'icon': 'fa-cogs',      'active': False},
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': True},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    secondary_navbar_options = ['']

    rol_id=get_roles(request.user.id)


    estado = request.session['estado']
    event_id = request.session['arbitraje_id']

    item_active = 4
    items=validate_rol_status(estado,rol_id,item_active)

    route_conf= get_route_configuracion(validate_rol_status(estado,rol_id,1))
    route_seg= get_route_seguimiento(validate_rol_status(estado,rol_id,2))
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)

    # print items

    context = {
        'nombre_vista' : 'Recursos',
        'main_navbar_options' : main_navbar_options,
        'secondary_navbar_options' : secondary_navbar_options,
        'estado' : estado,
        #'rol' : rol,
        'rol_id' : rol_id,
        'event_id' : event_id,
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
        'crear_trabajo_sidebar': items["crear_trabajo_sidebar"][0],
        'verify_configuration':items["configuration"][0],
        'verify_arbitration':items["arbitration"][0],
        'verify_result':items["result"][0],
        'verify_event':items["event"][0],
        'verify_jobs':items["jobs"][0],
        'route_conf':route_conf,
        'route_seg':route_seg,
    }
    return render(request, 'sesiones_space_list.html', context)

def sesions_space_edit(request):
    main_navbar_options = [{'title':'Configuración',   'icon': 'fa-cogs',      'active': False},
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': True},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    secondary_navbar_options = ['']
    
    rol_id=get_roles(request.user.id)


    estado = request.session['estado']
    event_id = request.session['arbitraje_id']

    item_active = 2
    items=validate_rol_status(estado,rol_id,item_active)

    route_conf= get_route_configuracion(validate_rol_status(estado,rol_id,1))
    route_seg= get_route_seguimiento(validate_rol_status(estado,rol_id,2))
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)

    # print items

    context = {
        'nombre_vista' : 'Recursos',
        'main_navbar_options' : main_navbar_options,
        'secondary_navbar_options' : secondary_navbar_options,
        'estado' : estado,
        #'rol' : rol,
        'rol_id' : rol_id,
        'event_id' : event_id,
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
        'crear_trabajo_sidebar': items["crear_trabajo_sidebar"][0],
        'verify_configuration':items["configuration"][0],
        'verify_arbitration':items["arbitration"][0],
        'verify_result':items["result"][0],
        'verify_event':items["event"][0],
        'verify_jobs':items["jobs"][0],
        'route_conf':route_conf,
        'route_seg':route_seg,
    }
    return render(request, 'sesiones_space_edit.html', context)