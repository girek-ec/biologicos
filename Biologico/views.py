from django.shortcuts import render
from Biologico.models import *
# Create your views here.

def index(request):
    contexto = {
                'biologicos': Marca.objects.all().first(),
                'edit_web' : Edit_pag.objects.all().first(),
                'sliders' : Slider.objects.all(),
                'productos': Producto.objects.all(),
                'beneficios':Beneficios_producto.objects.all(),
                'blogs':Blog.objects.all(),
                }

    return render(request, 'index.html', contexto)

def empresa(request):
    contexto = {
                'biologicos': Marca.objects.all().first(),
                'edit_web' : Edit_pag.objects.all().first(),
                'sliders' : Slider.objects.all(),
                'productos': Producto.objects.all(),
                'beneficios':Beneficios_producto.objects.all(),
                'blogs':Blog.objects.all(),
                }

    return render(request, 'page-about.html', contexto)

def servicios(request):
    contexto = {
                'biologicos': Marca.objects.all().first(),
                'edit_web' : Edit_pag.objects.all().first(),
                'sliders' : Slider.objects.all(),
                'productos': Producto.objects.all(),
                'beneficios':Beneficios_producto.objects.all(),
                'blogs':Blog.objects.all(),
                }

    return render(request, 'index.html', contexto)

def productos(request):
    contexto = {
                'biologicos': Marca.objects.all().first(),
                'edit_web' : Edit_pag.objects.all().first(),
                'sliders' : Slider.objects.all(),
                'productos': Producto.objects.all(),
                'beneficios':Beneficios_producto.objects.all(),
                'blogs':Blog.objects.all(),
                }

    return render(request, 'shop-products.html', contexto)


def producto_id(request,id):
    contexto = {
                'biologicos': Marca.objects.all().first(),
                'edit_web' : Edit_pag.objects.all().first(),
                'sliders' : Slider.objects.all(),
                'productos': Producto.objects.all(),
                'beneficios':Beneficios_producto.objects.all(),
                'blogs':Blog.objects.all(),
                }

    return render(request, 'page-project-details.html', contexto)

def contacto(request):
    contexto = {
                'biologicos': Marca.objects.all().first(),
                'edit_web' : Edit_pag.objects.all().first(),
                'sliders' : Slider.objects.all(),
                'productos': Producto.objects.all(),
                'beneficios':Beneficios_producto.objects.all(),
                'blogs':Blog.objects.all(),
                }

    return render(request, 'index.html', contexto)

def blog(request):
    contexto = {
                'biologicos': Marca.objects.all().first(),
                'edit_web' : Edit_pag.objects.all().first(),
                'sliders' : Slider.objects.all(),
                'productos': Producto.objects.all(),
                'beneficios':Beneficios_producto.objects.all(),
                'blogs':Blog.objects.all(),
                }

    return render(request, 'page-projects.html', contexto)

def post(request,n):
    contexto = {
                'biologicos': Marca.objects.all().first(),
                'edit_web' : Edit_pag.objects.all().first(),
                'sliders' : Slider.objects.all(),
                'productos': Producto.objects.all(),
                'beneficios':Beneficios_producto.objects.all(),
                'blogs':Blog.objects.get(id=n),
                }

    return render(request, 'page-project-details.html', contexto)