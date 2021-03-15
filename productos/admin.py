from django.contrib import admin
from .models import Categoria,Producto,Almacen

# Register your models here.
class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('nombre','cantidad','precio','foto','categoria')

class AlmacenesAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('nombre','telefono','email','ciudad','direccion','gerente')

admin.site.register(Categoria,CategoriasAdmin)
admin.site.register(Producto,ProductosAdmin)
admin.site.register(Almacen,AlmacenesAdmin)

