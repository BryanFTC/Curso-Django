from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'last_name', 'email']
        #fields = '__all__' esto nos incluira todos los campos.
        #extra_fields = [''] para agregar campos adicionales.
        #exclude = ('campo excluido', ,...) me devuelve todos los campos menos los mencionados dentro de ().