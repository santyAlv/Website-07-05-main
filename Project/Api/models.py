from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Categoría")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    # Relación con categoría (si se borra la categoría, el producto se queda sin categoría)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categoría")
    
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    
    # Precios y Stock (Usamos DecimalField para evitar errores de redondeo con dinero)
    precio = models.DecimalField(max_length=10, decimal_places=2, max_digits=10, verbose_name="Precio")
    stock = models.IntegerField(default=0, verbose_name="Cantidad en Stock")
    
    # Imagen del producto (se guardará en una carpeta 'productos/' dentro de tu Media)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, verbose_name="Imagen del Producto")
    
    # Fechas de control automático
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Alta")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Modificación")
    
    # Campo para activar/desactivar el producto sin borrarlo de la base de datos
    activo = models.BooleanField(default=True, verbose_name="¿Está Activo?")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_creacion'] # Muestra primero los más nuevos

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"