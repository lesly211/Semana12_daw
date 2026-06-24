from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto
from .forms import ProductoModelForm, ContactoForm

def home(request):
    """
    Vista principal que lista todos los productos registrados.
    """
    productos = Producto.objects.all().order_by('-fecha_creacion')
    return render(request, 'main/home.html', {'productos': productos})

def producto_nuevo(request):
    """
    Vista para registrar un nuevo producto usando el ModelForm.
    Maneja peticiones GET (mostrar formulario) y POST (guardar datos).
    """
    if request.method == 'POST':
        form = ProductoModelForm(request.POST)
        if form.is_valid():
            # Al ser ModelForm, form.save() crea e inserta el registro en la base de datos automáticamente
            producto = form.save()
            messages.success(request, f'¡Producto "{producto.nombre}" registrado con éxito!')
            return redirect('home')
    else:
        form = ProductoModelForm()
        
    return render(request, 'main/producto_form.html', {
        'form': form,
        'titulo': 'Registrar Producto (ModelForm)'
    })

def contacto(request):
    """
    Vista de contacto usando un formulario clásico (forms.Form).
    Maneja peticiones GET (mostrar formulario) y POST (validar y procesar).
    """
    datos_enviados = None
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Obtenemos los datos limpios y validados
            datos_enviados = form.cleaned_data
            messages.success(request, '¡Tu mensaje ha sido validado y enviado con éxito!')
            # En un caso real, aquí se enviaría un correo o se procesaría la consulta.
    else:
        form = ContactoForm()
        
    return render(request, 'main/contacto_form.html', {
        'form': form,
        'titulo': 'Formulario de Contacto (Formulario Clásico)',
        'datos_enviados': datos_enviados
    })
