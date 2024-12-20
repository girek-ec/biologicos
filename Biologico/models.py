from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.


class Edit_pag(models.Model):
    imag_fondo_slider = models.FileField(upload_to='slider/', null=True, blank=True, help_text="fondo slider  1894x718")
    imag_fondo_02 = models.FileField(upload_to='edit_web/', null=True, blank=True, help_text="fondo   1894x718")
    imag_fondo_03 = models.FileField(upload_to='edit_web/', null=True, blank=True, help_text="fondo  1894x718")
    imag_fondo_04 = models.FileField(upload_to='edit_web/', null=True, blank=True, help_text="fondo  1894x718")
    imag_fondo_05 = models.FileField(upload_to='edit_web/', null=True, blank=True, help_text="fondo  1894x718")
    imag_fondo_06 = models.FileField(upload_to='edit_web/', null=True, blank=True, help_text="fondo  1894x718")
    imag_pie = models.FileField(upload_to='edit_web/', null=True, blank=True, help_text="fondo  1894x718")
    ico_bene1 = models.CharField(max_length=100, null=True, blank=True)
    ico_titulo1 = models.CharField(max_length=100, null=True, blank=True)
    ico_subti1 = models.CharField(max_length=100, null=True, blank=True)
    ico_bene2 = models.CharField(max_length=100, null=True, blank=True)
    ico_titulo2 = models.CharField(max_length=100, null=True, blank=True)
    ico_subti2 = models.CharField(max_length=100, null=True, blank=True)
    ico_bene3 = models.CharField(max_length=100, null=True, blank=True)
    ico_titulo3 = models.CharField(max_length=100, null=True, blank=True)
    ico_subti3 = models.CharField(max_length=100, null=True, blank=True)
    ico_bene4 = models.CharField(max_length=100, null=True, blank=True)
    ico_titulo4 = models.CharField(max_length=100, null=True, blank=True)
    ico_subti4 = models.CharField(max_length=100, null=True, blank=True)
    about_img01 = models.FileField(upload_to='edit_web/', null=True, blank=True, help_text="fondo  1894x718")
    about_img02 = models.FileField(upload_to='edit_web/', null=True, blank=True, help_text="fondo  1894x718")
    about_sub_titulo1 = models.CharField(max_length=200, null=True, blank=True)
    about_titulo1 = models.CharField(max_length=200, null=True, blank=True)
    about_sub_titulo2 = models.CharField(max_length=200, null=True, blank=True)
    about_detalle1 = models.CharField(max_length=200, null=True, blank=True)
    about_destacado_01 = models.CharField(max_length=200, null=True, blank=True)
    about_destacado_02 = models.CharField(max_length=200, null=True, blank=True)
    about_destacado_03 = models.CharField(max_length=200, null=True, blank=True)
    about_destacado_04 = models.CharField(max_length=200, null=True, blank=True)
    img_mision = models.FileField(upload_to='edit_web/', null=True, blank=True, help_text="fondo  1894x718")
    mision = models.TextField(max_length=900, null=True, blank=True)
    img_vision = models.FileField(upload_to='edit_web/', null=True, blank=True, help_text="fondo  1894x718")
    vision = models.TextField(max_length=900, null=True, blank=True)
    class Meta:
        verbose_name_plural = "0. Edición de Pág Web"

class Marca(models.Model):
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=11, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    correo = models.EmailField()
    mapa = models.TextField(max_length=400, null=True, blank=True)
    facebook = models.CharField(max_length=80, null=True, blank=True)
    instagram = models.CharField(max_length=80, null=True, blank=True)
    tiktok = models.CharField(max_length=80, null=True, blank=True)
    youtube = models.CharField(max_length=80, null=True, blank=True)
    favicon = models.ImageField(upload_to='empresa/', null=True, blank=True)
    logo = models.ImageField(upload_to='empresa/', null=True, blank=True)
    logo_horiz_color = models.ImageField(upload_to='empresa/', null=True, blank=True)
    logo_horiz_verde = models.ImageField(upload_to='empresa/', null=True, blank=True)
    logo_horiz_blanco = models.ImageField(upload_to='empresa/', null=True, blank=True)
    logo_cuadrado = models.ImageField(upload_to='empresa/', null=True, blank=True)
    logo_cuadrado_verde = models.ImageField(upload_to='empresa/', null=True, blank=True)
    logo_cuadrado_blanco = models.ImageField(upload_to='empresa/', null=True, blank=True)


    def vista_previa(self):
        return mark_safe('<image width="300" height="150"  src="/media/%s">' % self.logo)

    class Meta:
        verbose_name_plural = "1. Biologicos "


class Slider(models.Model):
    orden = models.DecimalField(max_digits=2, decimal_places=0, default=0.00)
    titulo = models.CharField(max_length=90, null=True, blank=True)
    sub_titulo = models.CharField(max_length=90, null=True, blank=True)
    detalle = models.TextField(max_length=400, null=True, blank=True)
    img_izq_supe = models.FileField(upload_to='slider/', null=True, blank=True, help_text="slider  1600x964")
    img_der_supe_izq = models.FileField(upload_to='slider/', null=True, blank=True, help_text="slider  1600x964")
    img_der_supe_der = models.FileField(upload_to='slider/', null=True, blank=True, help_text="slider  1600x964")
    img_der_inf_izq_1 = models.FileField(upload_to='slider/', null=True, blank=True, help_text="slider  1600x964")
    img_der_inf_izq_2 = models.FileField(upload_to='slider/', null=True, blank=True, help_text="slider  1600x964")
    img_der_inf_der = models.FileField(upload_to='slider/', null=True, blank=True, help_text="slider  1600x964")
    imagen = models.FileField(upload_to='slider/', null=True, blank=True, help_text="slider  1600x964")
    link_video = models.CharField(max_length=200, null=True, blank=True, help_text="Link youtube")
   


    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "2. Slider "


class Producto(models.Model):
    titulo = models.CharField(max_length=90, null=True, blank=True)
    sub_titulo = models.CharField(max_length=90, null=True, blank=True)
    sub_titulo2 = models.CharField(max_length=90, null=True, blank=True)
    detalle = models.TextField(max_length=400, null=True, blank=True)
    utilizacion = models.TextField(max_length=1000, null=True, blank=True)
    antecedentes = models.TextField(max_length=1000, null=True, blank=True)
    ficha_tecnica = models.FileField(upload_to='producto/', null=True, blank=True, help_text="archivo pdf")
    nombre_certificacion = models.CharField(max_length=200, null=True, blank=True, help_text="Nombre de certificacion")
    certificacion = models.FileField(upload_to='producto/', null=True, blank=True,  help_text="archivo pdf")
    logo_certificacion = models.FileField(upload_to='producto/', null=True, blank=True, help_text="imagen certificacion")
    nombre_registro = models.CharField(max_length=200, null=True, blank=True, help_text="Nombre de registro")
    registro = models.FileField(upload_to='producto/', null=True, blank=True,  help_text="archivo pdf")
    logo_registro = models.FileField(upload_to='producto/', null=True, blank=True, help_text="imagen registro")
    logo_producto = models.FileField(upload_to='producto/', null=True, blank=True, help_text="logo")
    img_producto = models.FileField(upload_to='producto/', null=True, blank=True, help_text="imagen producto")
    img_set_producto = models.FileField(upload_to='producto/', null=True, blank=True, help_text="set producto")
    img_foto = models.FileField(upload_to='producto/', null=True, blank=True, help_text="foto")
    link_video = models.CharField(max_length=200, null=True, blank=True, help_text="Link youtube")
    litros_1 = models.BooleanField(default=False, null=True, blank=True)
    litros_4 = models.BooleanField(default=False, null=True, blank=True)
    litros_20 = models.BooleanField(default=False, null=True, blank=True)
    litros_200 = models.BooleanField(default=False, null=True, blank=True)
    img_fondo = models.FileField(upload_to='producto/', null=True, blank=True, help_text="producto fondo  ")
    img_foto01 = models.FileField(upload_to='producto/', null=True, blank=True, help_text="producto  571x570")
    img_foto02 = models.FileField(upload_to='producto/', null=True, blank=True, help_text="producto  270x270")
    izquierda = models.BooleanField(default=False, null=True, blank=True)
    derecha = models.BooleanField(default=False, null=True, blank=True)
    color = models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return ' %s ' % (self.titulo)

    def vista_previa(self):
        return mark_safe('<image width="100" height="250"  src="/media/%s">' % self.img_producto)

    class Meta:
        verbose_name_plural = "3. Producto "



class Servicio(models.Model):
    titulo = models.CharField(max_length=90, null=True, blank=True)
    sub_titulo_1 = models.CharField(max_length=90, null=True, blank=True)
    sub_titulo_2 = models.CharField(max_length=90, null=True, blank=True)
    parrafo_1 = models.TextField(max_length=1000, null=True, blank=True)
    parrafo_2 = models.TextField(max_length=1000, null=True, blank=True)
    beneficio_parrafo_1 = models.TextField(max_length=1000, null=True, blank=True)
    beneficio_1 = models.CharField(max_length=90, null=True, blank=True)
    beneficio_2 = models.CharField(max_length=90, null=True, blank=True)
    beneficio_3 = models.CharField(max_length=90, null=True, blank=True)
    beneficio_4 = models.CharField(max_length=90, null=True, blank=True)
    beneficio_5 = models.CharField(max_length=90, null=True, blank=True)
    beneficio_6 = models.CharField(max_length=90, null=True, blank=True)
    img_servicio_1 = models.FileField(upload_to='servicio/', null=True, blank=True, help_text="imagen servicio")
    img_servicio_2 = models.FileField(upload_to='servicio/', null=True, blank=True, help_text="imagen servicio")
    link_video_servicio = models.CharField(max_length=200, null=True, blank=True, help_text="Link youtube")
    color = models.CharField(max_length=90, null=True, blank=True)


    def __str__(self):
        return ' %s ' % (self.titulo)

    def vista_previa(self):
        return mark_safe('<image width="100" height="250"  src="/media/%s">' % self.img_servicio_1)

    class Meta:
        verbose_name_plural = "4. Servicios "

class Aplica_dosis_producto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    icono = models.FileField(upload_to='producto/', null=True, blank=True, help_text="icono  ")
    cultivo = models.CharField(max_length=100, null=True, blank=True)
    dosis = models.CharField(max_length=100, null=True, blank=True)
    aplicacion = models.TextField(max_length=400, null=True, blank=True)

    class Meta:
        verbose_name_plural = "4. Aplicación y dosis Productos "

class Beneficios_producto(models.Model):
    colum_izqui = models.BooleanField(default=False, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    detalle = models.TextField(max_length=400, null=True, blank=True)

    class Meta:
        verbose_name_plural = "4. Beneficios Productos "


class Blog(models.Model):

    titulo = models.CharField(max_length=150, null=True, blank=True)
    detalle = models.TextField(max_length=700, null=True, blank=True)
    autor = models.CharField(max_length=400, null=True, blank=True)
    imagen = models.FileField(upload_to='blog/', null=True, blank=True, help_text="blog  1600x964")
    fecha = models.DateField(   null=True, blank=True )
    def vista_previa(self):
        return mark_safe('<image width="100" height="250"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "5. Blog "