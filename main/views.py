from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from .models import Producto
from .forms import ProductoModelForm, ContactoForm

def home(request):
    productos = Producto.objects.all().order_by('-fecha_creacion')
    return render(request, 'main/home.html', {'productos': productos})

@login_required
def producto_nuevo(request):
    if request.method == 'POST':
        form = ProductoModelForm(request.POST)
        if form.is_valid():
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
    datos_enviados = None
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            datos_enviados = form.cleaned_data
            messages.success(request, '¡Tu mensaje ha sido validado y enviado con éxito!')
    else:
        form = ContactoForm()
    return render(request, 'main/contacto_form.html', {
        'form': form,
        'titulo': 'Formulario de Contacto (Formulario Clásico)',
        'datos_enviados': datos_enviados
    })

class InventarioAdminView(PermissionRequiredMixin, ListView):
    model = Producto
    template_name = 'main/inventario_admin.html'
    context_object_name = 'productos'
    permission_required = 'main.view_producto'
    raise_exception = True
