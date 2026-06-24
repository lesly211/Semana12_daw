from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import Producto
import re

def sanitize_input(value):
    if isinstance(value, str):
        return re.sub(r'<[^>]*>', '', value).strip()
    return value

class ProductoModelForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'disponible']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        nombre_sanitizado = sanitize_input(nombre)
        if len(nombre_sanitizado) < 3:
            raise ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre_sanitizado

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        return sanitize_input(descripcion)

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise ValidationError("El precio debe ser un valor positivo mayor a cero.")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise ValidationError("El stock no puede ser negativo.")
        return stock

    def clean(self):
        cleaned_data = super().clean()
        disponible = cleaned_data.get('disponible')
        stock = cleaned_data.get('stock')
        if disponible and stock == 0:
            raise ValidationError("No se puede marcar como disponible si el stock es cero.")
        return cleaned_data

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$', message="El nombre solo debe contener letras y espacios.")]
    )
    correo = forms.EmailField()
    asunto = forms.ChoiceField(
        choices=[
            ('SOPORTE', 'Soporte Técnico'),
            ('VENTAS', 'Información Comercial'),
            ('SUGERENCIA', 'Sugerencia'),
            ('RECLAMO', 'Reclamo')
        ]
    )
    mensaje = forms.CharField(widget=forms.Textarea)
    recibir_boletin = forms.BooleanField(required=False)

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        return sanitize_input(nombre)

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        return sanitize_input(mensaje)

    def clean(self):
        cleaned_data = super().clean()
        asunto = cleaned_data.get('asunto')
        mensaje = cleaned_data.get('mensaje')
        if asunto == 'RECLAMO' and mensaje and len(mensaje) < 20:
            raise ValidationError("Para un reclamo, detalle el mensaje con al menos 20 caracteres.")
        return cleaned_data
