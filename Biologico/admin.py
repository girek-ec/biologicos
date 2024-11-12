from django.contrib import admin

# Register your models here.
from Biologico.models import *
from biologicos.snippers import Attr


class Beneficios_productoInline(admin.StackedInline):
    model = Beneficios_producto
    extra = 0

class Aplica_dosis_productoInline(admin.StackedInline):
    model = Aplica_dosis_producto
    extra = 0


@admin.register(Edit_pag)
class Edit_pagAdmin(admin.ModelAdmin):
    list_display = Attr(Edit_pag) 
    list_display_links = Attr(Edit_pag)


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = Attr(Marca) + ["vista_previa"]
    list_display_links = Attr(Marca)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = Attr(Slider) + ["vista_previa"]
    list_display_links = Attr(Slider)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = Attr(Producto) + ["vista_previa"]
    list_display_links = Attr(Producto)
    inlines = [Beneficios_productoInline,Aplica_dosis_productoInline ]


@admin.register(Beneficios_producto)
class Beneficios_productoAdmin(admin.ModelAdmin):
    list_display = Attr(Beneficios_producto) 
    list_display_links = Attr(Beneficios_producto)

@admin.register(Aplica_dosis_producto)
class Aplica_dosis_productoAdmin(admin.ModelAdmin):
    list_display = Attr(Aplica_dosis_producto)
    list_display_links = Attr(Aplica_dosis_producto)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = Attr(Blog) + ["vista_previa"]
    list_display_links = Attr(Blog)