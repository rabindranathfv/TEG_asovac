# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from django import forms
from django.core.urlresolvers import reverse

from .models import Sistema_asovac

class MyLoginForm(forms.Form):
    username = forms.CharField(label="Usuario", max_length=100)
    password = forms.CharField(label="Contraseña", max_length=100, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'login-form'
        self.helper.form_method = 'post'
        #self.helper.form_action = reverse('/') # <-- CHANGE THIS LINE TO THE NAME OF LOGIN VIEW
        self.helper.add_input(Submit('submit', 'Ingresar', css_class='btn-block'))

class CreateArbitrajeForm(forms.ModelForm):

    class Meta:
        model = Sistema_asovac
        fields = ['nombre','descripcion', 'fecha_inicio_arbitraje', 'fecha_fin_arbitraje']

    def __init__(self, *args, **kwargs):
        super(CreateArbitrajeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'create-arbitraje-form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-8'
        #self.helper.form_action = reverse('/') # <-- CHANGE THIS LINE TO THE NAME OF LOGIN VIEW
        self.helper.add_input(Submit('submit', 'Crear', css_class='btn-success btn-lg pull-right'))
        self.helper.layout = Layout( # the order of the items in this layout is important
            'nombre',
            Field('descripcion', rows="4"),
            'fecha_inicio_arbitraje',
            'fecha_fin_arbitraje',
        )

