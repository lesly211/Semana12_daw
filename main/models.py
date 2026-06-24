from django.db import models

class Producto(models.Model):
    CATEGORIAS = [
        ('ELECTRONICA', 'Electrónica'),
        ('ROPA', 'Ropa y Calzado'),
        ('HOGAR', 'Hogar y Cocina'),
        ('LIBROS', 'Libros y Papelería'),
        ('OTROS', 'Otros'),
    ]
    
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Producto")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio (S/.)")
    stock = models.IntegerField(verbose_name="Stock Disponible")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='OTROS', verbose_name="Categoría")
    disponible = models.BooleanField(default=True, verbose_name="¿Está disponible para la venta?")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} (Stock: {self.stock})"
