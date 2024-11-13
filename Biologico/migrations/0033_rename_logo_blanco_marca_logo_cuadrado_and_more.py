# Generated by Django 4.0.6 on 2024-11-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biologico', '0032_remove_aplica_dosis_producto_img_foto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marca',
            old_name='logo_blanco',
            new_name='logo_cuadrado',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='logo_horiz',
            new_name='logo_cuadrado_blanco',
        ),
        migrations.AddField(
            model_name='marca',
            name='logo_cuadrado_verde',
            field=models.ImageField(blank=True, null=True, upload_to='empresa/'),
        ),
        migrations.AddField(
            model_name='marca',
            name='logo_horiz_blanco',
            field=models.ImageField(blank=True, null=True, upload_to='empresa/'),
        ),
        migrations.AddField(
            model_name='marca',
            name='logo_horiz_color',
            field=models.ImageField(blank=True, null=True, upload_to='empresa/'),
        ),
        migrations.AddField(
            model_name='marca',
            name='logo_horiz_verde',
            field=models.ImageField(blank=True, null=True, upload_to='empresa/'),
        ),
    ]
