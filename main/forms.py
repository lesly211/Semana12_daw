from django import forms
from .models import Producto

class ProductoModelForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej. Smart TV 55" LG'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe una breve descripción del producto...'}),
            'precio': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'placeholder': 'Ej. 25'}),
        }
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción Detallada',
            'precio': 'Precio en Soles (S/.)',
            'stock': 'Cantidad en Stock',
            'categoria': 'Categoría',
            'disponible': '¿Está disponible para la venta?',
        }

class ContactoForm(forms.Form):
    ASUNTOS = [
        ('SOPORTE', 'Soporte Técnico'),
        ('VENTAS', 'Información Comercial'),
        ('SUGERENCIA', 'Sugerencias y Comentarios'),
        ('RECLAMO', 'Reclamaciones'),
    ]
    
    nombre = forms.CharField(
        max_length=100,
        label="Tu Nombre Completo",
        widget=forms.TextInput(attrs={'placeholder': 'Ej. Lesly Quispe'})
    )
    correo = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={'placeholder': 'lesly@example.com'})
    )
    asunto = forms.ChoiceField(
        choices=ASUNTOS,
        label="Asunto de la Consulta",
        initial='SUGERENCIA'
    )
    mensaje = forms.CharField(
        label="Mensaje o Consulta",
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe aquí tu consulta o comentario...'})
    )
    recibir_boletin = forms.BooleanField(
        required=False,
        label="Deseo suscribirme al boletín de novedades",
        initial=True
    )
