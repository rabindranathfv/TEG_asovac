# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit, Div, HTML
from django import forms
from django.core.urlresolvers import reverse

from .models import Trabajo


#Form para introducir datos de un trabajo, sea para editar o para crear
class TrabajoForm(forms.ModelForm):

	class Meta:
		model = Trabajo
		fields = ['titulo_espanol', 'titulo_ingles', 'palabras_clave', 'forma_presentacion', 'area', 'subarea1', 'subarea2', 'subarea3', 'resumen', 'documento_inscrito', 'observaciones', 'url_trabajo', 'version', 'archivo_trabajo']

	def __init__(self, *args, **kwargs):
		super(TrabajoForm,self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'trabajo-form'
		self.helper.form_method = 'post'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-sm-3'
		self.helper.field_class = 'col-sm-8'
		self.fields['titulo_espanol'].label = "Título español"
		self.fields['titulo_ingles'].label = "Título inglés"
		self.fields['forma_presentacion'].label = "Forma de presentación"
		self.fields['area'].label = "Área"
		self.fields['subarea1'].label = "Subárea 1"
		self.fields['subarea2'].label = "Subárea 2"
		self.fields['subarea3'].label = "Subárea 3"
		self.fields['version'].label = "Versión"
		self.fields['archivo_trabajo'].label = "Archivo del trabajo"
		self.helper.layout = Layout(
			Div(	
				Div(
					'titulo_espanol',
					'titulo_ingles',
					'palabras_clave',
					'forma_presentacion',
					'area',
					'subarea1',
					'subarea2',
					'subarea3',
					'archivo_trabajo',
					css_class='col-sm-6',
					),
				Div(
					'version',
					'url_trabajo',
					'documento_inscrito',
					Field('resumen', rows="4"),			
					Field('observaciones', rows="4"),
					css_class='col-sm-6',
				),
				css_class='row'
			),
			HTML("<div class=\"col-sm-2 col-sm-offset-8\"><a href=\"#accordion\" class=\"btn btn-danger btn-block btn-lg\" data-toggle=\"collapse\">Cancelar</a></div><div class=\"col-sm-2\"><button type=\"button\" class=\"btn btn-primary btn-success btn-lg btn-block\" data-toggle=\"modal\" data-target=\"#ModalCenter\">Guardar</button></div>"),
			HTML("<div class=\"modal fade\" id=\"ModalCenter\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"ModalCenterTitle\" aria-hidden=\"true\"><div class=\"modal-dialog modal-dialog-centered\" role=\"document\"><div class=\"modal-content\"><div class=\"modal-header\"><h3 class=\"modal-title\" id=\"ModalLongTitle\">Postular Trabajo</h5><button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button></div><div class=\"modal-body text-center content-modal\">¿Está seguro que desea postular el trabajo?</div><div class=\"modal-footer\"><button type=\"button\" class=\"btn btn-secondary btn-danger\" data-dismiss=\"modal\">Cancelar</button><button type=\"submit\" class=\"btn btn-primary btn-success\">Postular</button></div></div></div></div>"),
			)
