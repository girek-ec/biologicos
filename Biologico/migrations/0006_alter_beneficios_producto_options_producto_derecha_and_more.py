# Generated by Django 4.0.6 on 2024-10-02 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biologico', '0005_alter_producto_options_producto_img_fondo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beneficios_producto',
            options={'verbose_name_plural': '4. Beneficios Productos '},
        ),
        migrations.AddField(
            model_name='producto',
            name='derecha',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='izquierda',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]