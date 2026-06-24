from django.contrib import admin
from .models import Producto

@admin.action(description="Marcar como disponibles")
def marcar_disponible(modeladmin, request, queryset):
    queryset.update(disponible=True)

@admin.action(description="Marcar como no disponibles")
def marcar_no_disponible(modeladmin, request, queryset):
    queryset.update(disponible=False)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'disponible', 'valor_inventario')
    list_filter = ('categoria', 'disponible', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('fecha_creacion',)
    actions = [marcar_disponible, marcar_no_disponible]

    @admin.display(description="Valor del Inventario (S/.)", ordering="precio")
    def valor_inventario(self, obj):
        return obj.precio * obj.stock
