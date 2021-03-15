from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

def url_producto(self,filename):
    ruta = "static/img/Productos/%s/%s"%(self.nombre,str(filename))
    return ruta

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    precio = models.DecimalField(decimal_places=2,max_digits=4)
    imagen=models.ImageField(upload_to=url_producto,null=True,blank=True) #Le ponemos esos atributos para que sea opcional la imagen
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE, default='available')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def foto(self):
        if self.imagen:
            return mark_safe('<a href="/%s" ><img src="/%s" height="50px" width="50px" /></a>' % (self.imagen, self.imagen))
        else:
            return mark_safe('No hay Imagen')

    foto.allow_tags = True

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre

ciudades = [
    ('Zamora','Zamora'),
    ('Loja','Loja'),
    ('Zumbi','Zumbi'),
    ('Cuenca','Cuenca'),
    ('Quito','Quito'),
    ('Guayaquil','Guayaquil'),
    ('Ambato','Ambato'),
    ('Portoviejo','Portoviejo'),
    ('Machala','Machala'),
    ('Yanzatza','Yanzatza'),
]

class Almacen(models.Model):
    nombre=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()
    ciudad=models.CharField(max_length=20,choices=ciudades,default='available')
    direccion=models.CharField(max_length=100)
    gerente=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    productos=models.ManyToManyField(Producto)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='almacen'
        verbose_name_plural='almacenes'

    def __str__(self):
        return self.nombre