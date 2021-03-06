# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from main_app.models import Usuario_asovac, Sistema_asovac,Rol
from main_app.views import get_route_resultados, get_route_trabajos_navbar, get_route_trabajos_sidebar, get_roles, get_route_configuracion, get_route_seguimiento, validate_rol_status

#Import forms
from .forms import EditOrganizerForm,CreateOrganizerForm,CreateEventForm,CreateLocacionForm, EditEventForm, AddOrganizerToEventForm, AddObservationsForm

#Import Models
from .models import Organizador,Organizador_evento,Evento,Locacion_evento


# Event's home
@login_required
def home(request):
    #Métricas de eventos
    last_events = Evento.objects.all().order_by('-id')[:5]
    total_events = Evento.objects.all().count()
    events_list = Evento.objects.all()
    current_date = datetime.datetime.now().date()
    total_events_ended = 0
    total_presential_events = 0
    total_virtual_events = 0
    for event in events_list:
        if (event.fecha_fin < current_date):
            total_events_ended += 1
        if (event.categoria == 'P'):
            total_presential_events += 1
        else:
            total_virtual_events += 1

    #Métricas de organizadores
    last_organizers = Organizador.objects.all().order_by('-id')[:5]
    total_organizers = Organizador.objects.all().count()
    organizer_list = Organizador.objects.all()
    total_organizers_members = 0
    for organizer in organizer_list:
        if(organizer.es_miembro_asovac):
            total_organizers_members += 1

    #Métricas de locaciones
    last_locations = Locacion_evento.objects.all().order_by('-id')[:5]
    total_locations = Locacion_evento.objects.all().count()
    location_list = Locacion_evento.objects.all()
    average_capacity = 0
    max_capacity_location = 0
    for location in location_list:
        if(max_capacity_location < location.capacidad_de_asistentes):
            max_capacity_location = location.capacidad_de_asistentes
        average_capacity += location.capacidad_de_asistentes
    if(location_list):
        average_capacity /= total_locations

    context = {
        'last_events':last_events,
        'total_events':total_events,
        'total_events_ended':total_events_ended,
        'total_presential_events': total_presential_events,
        'total_virtual_events': total_virtual_events,

        'last_organizers':last_organizers,
        'total_organizers':total_organizers,
        'total_organizers_members':total_organizers_members,

        'last_locations':last_locations,
        'total_locations':total_locations,
        'max_capacity_location': max_capacity_location,
        'average_capacity': average_capacity,

        'events_app': True,
    }
    return render(request, 'events_home.html', context)



@login_required
# Create your views here.
def event_create(request):
    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            fecha_preferida = form.cleaned_data['fecha_preferida']
            dia_asignado = form.cleaned_data['dia_asignado']
            if fecha_inicio <= fecha_fin and fecha_inicio <= dia_asignado and fecha_inicio <= fecha_preferida and dia_asignado <= fecha_fin and fecha_preferida <= fecha_fin:
                evento = form.save()
                locacion_preferida = form.cleaned_data['locacion_preferida']
                email_organizador = form.cleaned_data['email_organizador']

                organizador = Organizador.objects.get(correo_electronico = email_organizador)
                organizador_evento = Organizador_evento(organizador = organizador, evento = evento, locacion_preferida = locacion_preferida)
                organizador_evento.save()
                print("El form es valido y se guardo satisfactoriamente el EVENTO")
                return redirect(reverse('eventos:event_list')) 
            else:
                if fecha_fin < fecha_inicio:
                    messages.error(request, "La fecha final del evento no puede ser anterior a la fecha de inicio")
                else:    
                    if fecha_preferida < fecha_inicio or fecha_fin < fecha_preferida:
                        messages.error(request, "La fecha preferida está fuera del rango del evento")
                    if dia_asignado < fecha_inicio or fecha_fin < dia_asignado:
                        messages.error(request, "El día asignado está fuera del rango del evento")
                
    
    else:
        form = CreateEventForm()
    context = {
        'username' : request.user.username,
        'form' : form,
        'events_app': True,
    }
    return render(request, 'eventos_event_create.html',context)



@login_required
def event_list(request):
    event_data = Evento.objects.all().order_by('-id')
    #for data in event_data:
        #print("nombre " + data.nombre)
    context = {
        'nombre_vista' : 'Eventos',
        'username': request.user.username,
        'event_data': event_data,
        'events_app': True,
    }
    return render(request, 'eventos_event_list.html', context)



@login_required
def event_edit(request, evento_id):
    evento = get_object_or_404(Evento,id = evento_id)
    if request.method == 'POST':
        form = EditEventForm(request.POST, instance = evento)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            fecha_preferida = form.cleaned_data['fecha_preferida']
            dia_asignado = form.cleaned_data['dia_asignado']
            if fecha_inicio <= fecha_fin and fecha_inicio <= dia_asignado and fecha_inicio <= fecha_preferida and dia_asignado <= fecha_fin and fecha_preferida <= fecha_fin:
                form.save()
                return redirect(reverse('eventos:event_list'))
            else:
                if fecha_fin < fecha_inicio:
                    messages.error(request, "La fecha final del evento no puede ser anterior a la fecha de inicio")
                else:
                    if fecha_preferida < fecha_inicio or fecha_fin < fecha_preferida:
                        messages.error(request, "La fecha preferida está fuera del rango del evento")
                    if dia_asignado < fecha_inicio or fecha_fin < dia_asignado:
                        messages.error(request, "El día asignado está fuera del rango del evento")
                

    form = EditEventForm(instance = evento)   
    context = {
        'nombre_vista' : 'Autores',
        'username': request.user.username,
        'form':form,
        'events_app': True,
        }
    return render(request, 'eventos_event_edit.html', context)



@login_required
def event_delete(request, evento_id):
    data = dict()
    evento = get_object_or_404(Evento, id = evento_id)
    if request.method == "POST":
        evento.delete()
        return redirect(reverse('eventos:event_list')) 
    else:
        context = {
            'evento':evento,
        }
        data['html_form'] = render_to_string('ajax/event_delete.html',context,request=request)
    return JsonResponse(data)



@login_required
def event_detail(request, evento_id):
    evento = get_object_or_404(Evento, id = evento_id)
    organizador_evento_list = Organizador_evento.objects.filter(evento = evento)
    context = {
        'nombre_vista' : 'Autores',
        'username': request.user.username,
        'evento': evento,
        'organizador_evento_list': organizador_evento_list,
        'events_app': True,
    }
    return render(request, 'eventos_event_detail.html',context)  



##################### Organizer Views ###########################
@login_required
def organizer_create(request):
    form = CreateOrganizerForm()

    if request.method == 'POST':
        form = CreateOrganizerForm(request.POST)
        if form.is_valid():
            organizador = form.save(commit=False)
            user = request.user
            usuario_asovac = get_object_or_404(Usuario_asovac,usuario = user)
            organizador.usuario_asovac = usuario_asovac
            organizador.save()
            return redirect(reverse('eventos:organizer_list')) 
    
    context = {
        'username' : request.user.username,
        'form' : form,
        'events_app': True,
    }
    
    return render(request, 'eventos_organizer_create.html',context)



@login_required
def organizer_list(request):
    organizer_data = Organizador.objects.all().order_by('-id')
    usuario_asovac = Usuario_asovac.objects.get(usuario = request.user)
    context = {        
                'username' : request.user.username,
                'organizer_data': organizer_data,
                'usuario_asovac':usuario_asovac,
                'events_app': True,
                }
    return render(request, 'eventos_organizer_list.html', context)



@login_required
def organizer_edit(request, organizador_id):
    organizador = get_object_or_404(Organizador,id = organizador_id)
    if request.method == 'POST':
        form = EditOrganizerForm(request.POST, organizer = organizador, instance = organizador)
        if form.is_valid():
            form.save()
            return redirect(reverse('eventos:organizer_list'))
    else:
        form = EditOrganizerForm(organizer = organizador,instance = organizador)   
    context = {
        'nombre_vista' : 'Autores',
        'username': request.user.username,
        'form':form,
        'events_app': True,
        }
    return render(request, 'eventos_organizer_edit.html', context)



@login_required
def organizer_delete(request, organizador_id):
    data = dict()
    organizador= get_object_or_404(Organizador, id = organizador_id)
    if request.method == "POST":
        organizador.delete()
        return redirect(reverse('eventos:organizer_list')) 
    else:
        context = {
            'organizador':organizador,
        }
        data['html_form'] = render_to_string('ajax/organizer_delete.html',context,request=request)
    return JsonResponse(data)



@login_required
def organizer_detail(request, organizador_id):
    data = dict()
    organizador= get_object_or_404(Organizador, id = organizador_id)
    context = {
            'organizador':organizador,
        }
    data['html_form'] = render_to_string('ajax/organizer_details.html',context,request=request)
    return JsonResponse(data)



##################### Locacion Views ###########################
@login_required
def event_place_create(request):
    

    if request.method == 'POST':
        form = CreateLocacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('eventos:event_place_list'))
    else: 
        form = CreateLocacionForm()
    context = {
        'nombre_vista' : 'Crear locación de evento',
        'username': request.user.username,
        'form': form,
        'events_app': True,
    }
    return render(request, 'eventos_locacion_create.html', context)



@login_required
def event_place_list(request):
    event_place_data = Locacion_evento.objects.all().order_by('id')
    context = {        
                'username' : request.user.username,
                'event_place_data': event_place_data,
                'events_app': True,
                }
    return render(request, 'eventos_locacion_list.html', context)



@login_required
def event_place_edit(request, locacion_id):
    locacion = get_object_or_404(Locacion_evento,id = locacion_id)
    if request.method == 'POST':
        form = CreateLocacionForm(request.POST, instance = locacion)
        if form.is_valid():
            form.save()
            return redirect(reverse('eventos:event_place_list'))
    else:
        form = CreateLocacionForm(instance = locacion)   
    context = {
        'nombre_vista' : 'Autores',
        'username': request.user.username,
        'form':form,
        'events_app': True,
        }
    return render(request, 'eventos_locacion_edit.html', context)



@login_required
def event_place_delete(request, locacion_id):
    data = dict()
    locacion = get_object_or_404(Locacion_evento, id = locacion_id)
    if request.method == "POST":
        locacion.delete()
        return redirect(reverse('eventos:event_place_list')) 
    else:
        context = {
            'locacion':locacion,
        }
        data['html_form'] = render_to_string('ajax/location_delete.html',context,request=request)
    return JsonResponse(data)



@login_required
def event_place_detail(request, locacion_id):
    locacion = get_object_or_404(Locacion_evento, id = locacion_id)
    
    context = {
        'nombre_vista' : 'Autores',
        'username': request.user.username,
        'locacion': locacion,
        'events_app': True,
    }
    return render(request, 'eventos_locacion_details.html', context)



@login_required
def add_organizer_to_event(request, evento_id):
    data = dict()
    evento = get_object_or_404(Evento, id = evento_id)
    if request.method == 'POST':
        form = AddOrganizerToEventForm(request.POST, event = evento)
        if form.is_valid():
            form_data = form.cleaned_data
            organizador = get_object_or_404(Organizador, correo_electronico = form_data['correo_electronico'])
            organizador_evento = Organizador_evento(organizador = organizador, evento = evento, locacion_preferida = form_data['locacion_preferida'])
            organizador_evento.save()
            messages.success(request, 'El organizador fue añadido con éxito al evento.')
            data['url'] = reverse('eventos:event_list')
            data['form_is_valid'] = True
    else:
        form = AddOrganizerToEventForm(event = evento) 
    context = {
        'nombre_vista' : 'Autores',
        'username': request.user.username,
        'evento':evento,
        'form':form
        }
    data['html_form'] = render_to_string('ajax/add_organizer_to_event.html',context,request=request)
    return JsonResponse(data)



@login_required
def add_observations_to_event(request, evento_id):
    data = dict()
    evento = get_object_or_404(Evento, id = evento_id)
    if request.method == 'POST':
        form = AddObservationsForm(request.POST)
        if form.is_valid():
            evento.observaciones = form.cleaned_data['observaciones']
            evento.save()
            messages.success(request, 'Las observaciones fueron añadidas con éxito.')
            return redirect(reverse('eventos:event_list'))
    else:
        form = AddObservationsForm(initial={'observaciones': evento.observaciones}) 
        context = {
            'nombre_vista' : 'Autores',
            'username': request.user.username,
            'evento':evento,
            'form':form
            }
        data['html_form'] = render_to_string('ajax/add_observations_to_event.html',context,request=request)
    return JsonResponse(data)



@login_required
def add_observations_to_event_place(request, locacion_id):
    data = dict()
    locacion = get_object_or_404(Locacion_evento, id = locacion_id)
    if request.method == 'POST':
        form = AddObservationsForm(request.POST)
        if form.is_valid():
            locacion.observaciones = form.cleaned_data['observaciones']
            locacion.save()
            messages.success(request, 'Las observaciones fueron añadidas con éxito.')
            return redirect(reverse('eventos:event_place_list'))
    else:
        form = AddObservationsForm(initial={'observaciones': locacion.observaciones}) 
        context = {
            'nombre_vista' : 'Autores',
            'username': request.user.username,
            'locacion':locacion,
            'form':form
            }
        data['html_form'] = render_to_string('ajax/add_observations_to_event_place.html',context,request=request)
    return JsonResponse(data)



@login_required
def add_observations_to_organizer(request, organizador_id):
    data = dict()
    organizador = get_object_or_404(Organizador, id = organizador_id)
    if request.method == 'POST':
        form = AddObservationsForm(request.POST)
        if form.is_valid():
            organizador.observaciones = form.cleaned_data['observaciones']
            organizador.save()
            messages.success(request, 'Las observaciones fueron añadidas con éxito.')
            return redirect(reverse('eventos:organizer_list'))
    else:
        form = AddObservationsForm(initial={'observaciones': organizador.observaciones}) 
        context = {
            'nombre_vista' : 'Autores',
            'username': request.user.username,
            'organizador':organizador,
            'form':form
            }
        data['html_form'] = render_to_string('ajax/add_observations_to_organizer.html',context,request=request)
    return JsonResponse(data)



@login_required
def arbitraje_places_list(request):
    main_navbar_options = [{'title':'Configuración','icon': 'fa-cogs','active': True },
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': False},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    arbitraje_id = request.session['arbitraje_id']
    arbitraje = Sistema_asovac.objects.get(pk=arbitraje_id)
    estado = arbitraje.estado_arbitraje
    rol_id=get_roles(request.user.id,arbitraje_id)

    item_active = 5
    items=validate_rol_status(estado,rol_id,item_active, arbitraje_id)

    route_conf= get_route_configuracion(estado,rol_id, arbitraje_id)
    route_seg= get_route_seguimiento(estado,rol_id)
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)
    route_trabajos_navbar = get_route_trabajos_navbar(estado,rol_id)
    route_resultados = get_route_resultados(estado,rol_id, arbitraje_id)

    
    context = {
        'nombre_vista' : 'Locaciones de arbitraje',
        'main_navbar_options' : main_navbar_options,
        'estado' : estado,
        'rol_id' : rol_id,
        'arbitraje_id' : arbitraje_id,
        'item_active' : item_active,
        'items':items,
        'route_conf':route_conf,
        'route_seg':route_seg,
        'route_trabajos_sidebar':route_trabajos_sidebar,
        'route_trabajos_navbar': route_trabajos_navbar,
        'route_resultados': route_resultados,
    }
    return render(request,"eventos_locacion_list.html",context)



@login_required
def arbitraje_organizers_list(request):
    main_navbar_options = [{'title':'Configuración','icon': 'fa-cogs','active': True },
                    {'title':'Monitoreo',       'icon': 'fa-eye',       'active': False},
                    {'title':'Resultados',      'icon': 'fa-chart-area','active': False},
                    {'title':'Administración',  'icon': 'fa-archive',   'active': False}]

    arbitraje_id = request.session['arbitraje_id']
    arbitraje = Sistema_asovac.objects.get(pk=arbitraje_id)
    estado = arbitraje.estado_arbitraje
    rol_id=get_roles(request.user.id,arbitraje_id)

    item_active = 5
    items=validate_rol_status(estado,rol_id,item_active, arbitraje_id)

    route_conf= get_route_configuracion(estado,rol_id, arbitraje_id)
    route_seg= get_route_seguimiento(estado,rol_id)
    route_trabajos_sidebar = get_route_trabajos_sidebar(estado,rol_id,item_active)
    route_trabajos_navbar = get_route_trabajos_navbar(estado,rol_id)
    route_resultados = get_route_resultados(estado,rol_id, arbitraje_id)

    
    context = {
        'nombre_vista' : 'Organizadores de eventos del arbitraje',
        'main_navbar_options' : main_navbar_options,
        'estado' : estado,
        'rol_id' : rol_id,
        'arbitraje_id' : arbitraje_id,
        'item_active' : item_active,
        'items':items,
        'route_conf':route_conf,
        'route_seg':route_seg,
        'route_trabajos_sidebar':route_trabajos_sidebar,
        'route_trabajos_navbar': route_trabajos_navbar,
        'route_resultados': route_resultados,
    }
    return render(request,"eventos_organizer_list.html",context)