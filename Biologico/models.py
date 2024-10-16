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
    favicon = models.ImageField(upload_to='empresa/', null=True, blank=True)
    logo=models.ImageField(upload_to='empresa/', null=True, blank=True)
    logo_horiz=models.ImageField(upload_to='empresa/', null=True, blank=True)
    logo_blanco=models.ImageField(upload_to='empresa/', null=True, blank=True)
    mision = models.TextField(max_length=400, null=True, blank=True)
    vision = models.TextField(max_length=400, null=True, blank=True)
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=11, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)
    correo = models.EmailField()
    facebook = models.TextField(max_length=100, null=True, blank=True)
    instagram = models.TextField(max_length=100, null=True, blank=True)
    tiktok = models.TextField(max_length=100, null=True, blank=True)
    youtube = models.TextField(max_length=100, null=True, blank=True)



    def vista_previa(self):
        return mark_safe('<image width="300" height="150"  src="/media/%s">' % self.logo)

    class Meta:
        verbose_name_plural = "1. Biologicos "


class Slider(models.Model):
    img_izq_supe = models.FileField(upload_to='slider/', null=True, blank=True,help_text="slider  1600x964")
    img_der_supe_izq = models.FileField(upload_to='slider/', null=True, blank=True,help_text="slider  1600x964")
    img_der_supe_der = models.FileField(upload_to='slider/', null=True, blank=True,help_text="slider  1600x964")
    img_der_inf_izq_1 = models.FileField(upload_to='slider/', null=True, blank=True,help_text="slider  1600x964")
    img_der_inf_izq_2 = models.FileField(upload_to='slider/', null=True, blank=True,help_text="slider  1600x964")
    img_der_inf_der = models.FileField(upload_to='slider/', null=True, blank=True,help_text="slider  1600x964")
    imagen = models.FileField(upload_to='slider/', null=True, blank=True,help_text="slider  1600x964")
    link_video = models.CharField(max_length=200, null=True, blank=True,help_text="Link youtube")
    titulo = models.CharField(max_length=90, null=True, blank=True)
    sub_titulo = models.CharField(max_length=90, null=True, blank=True)
    detalle = models.TextField(max_length=400, null=True, blank=True)
   


    def vista_previa(self):
        return mark_safe('<image width="300" height="150"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "2. Slider "


class Producto(models.Model):
    logo_producto = models.FileField(upload_to='producto/', null=True, blank=True, help_text="slider  1600x964")
    img_producto = models.FileField(upload_to='producto/', null=True, blank=True, help_text="slider  1600x964")
    img_set_producto = models.FileField(upload_to='producto/', null=True, blank=True, help_text="slider  1600x964")
    img_foto = models.FileField(upload_to='producto/', null=True, blank=True, help_text="slider  1600x964")
    link_video = models.CharField(max_length=200, null=True, blank=True, help_text="Link youtube")
    titulo = models.CharField(max_length=90, null=True, blank=True)
    sub_titulo = models.CharField(max_length=90, null=True, blank=True)
    sub_titulo2 = models.CharField(max_length=90, null=True, blank=True)
    detalle = models.TextField(max_length=400, null=True, blank=True)
    img_fondo = models.FileField(upload_to='producto/', null=True, blank=True, help_text="producto fondo  ")
    img_foto01 = models.FileField(upload_to='producto/', null=True, blank=True, help_text="producto  571x570")
    img_foto02 = models.FileField(upload_to='producto/', null=True, blank=True, help_text="producto  270x270")
    izquierda = models.BooleanField(default=False, null=True, blank=True)
    derecha = models.BooleanField(default=False, null=True, blank=True)
    color = models.CharField(max_length=90, null=True, blank=True)
    def vista_previa(self):
        return mark_safe('<image width="100" height="250"  src="/media/%s">' % self.img_producto)

    class Meta:
        verbose_name_plural = "3. Producto "



class Beneficios_producto(models.Model):
    colum_izqui = models.BooleanField(default=False, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    detalle = models.TextField(max_length=400, null=True, blank=True)

    class Meta:
        verbose_name_plural = "4. Beneficios Productos "



class Blog(models.Model):
    imagen = models.FileField(upload_to='blog/', null=True, blank=True, help_text="blog  1600x964")
    titulo = models.CharField(max_length=100, null=True, blank=True)
    detalle = models.TextField(max_length=400, null=True, blank=True)
    autor = models.CharField(max_length=400, null=True, blank=True)
    fecha = models.DateField(   null=True, blank=True )
    def vista_previa(self):
        return mark_safe('<image width="100" height="250"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "5. Blog "