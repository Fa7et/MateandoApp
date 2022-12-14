from tkinter import E
from django.contrib import admin
from .models import Avatar, Usuario, Yerba, Canal, CanalMensaje, CanalUsuario, Posteo  
# Register your models here.


class CanalMensajeInline(admin.TabularInline):
    model=CanalMensaje
    extra=1

class CanalUsuarioInline(admin.TabularInline):
    model=CanalUsuario
    Extra=1

class CanalAdmin(admin.ModelAdmin):
    inlines= [CanalMensajeInline, CanalUsuarioInline]

    class Meta:
        model= Canal


admin.site.register(Usuario)
admin.site.register(Yerba)
admin.site.register(Avatar)
admin.site.register(Canal, CanalAdmin)
admin.site.register(CanalMensaje)
admin.site.register(CanalUsuario)
admin.site.register(Posteo) 

