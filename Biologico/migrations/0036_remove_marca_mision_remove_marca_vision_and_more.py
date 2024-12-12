# Generated by Django 4.0.6 on 2024-12-04 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biologico', '0035_alter_marca_facebook_alter_marca_instagram_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marca',
            name='mision',
        ),
        migrations.RemoveField(
            model_name='marca',
            name='vision',
        ),
        migrations.AddField(
            model_name='producto',
            name='certificacion',
            field=models.FileField(blank=True, help_text='archivo pdf', null=True, upload_to='producto/'),
        ),
        migrations.AddField(
            model_name='producto',
            name='registro',
            field=models.FileField(blank=True, help_text='archivo pdf', null=True, upload_to='producto/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='ficha_tecnica',
            field=models.FileField(blank=True, help_text='archivo pdf', null=True, upload_to='producto/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='img_foto',
            field=models.FileField(blank=True, help_text='foto', null=True, upload_to='producto/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='img_producto',
            field=models.FileField(blank=True, help_text='imagen producto', null=True, upload_to='producto/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='img_set_producto',
            field=models.FileField(blank=True, help_text='set producto', null=True, upload_to='producto/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='logo_producto',
            field=models.FileField(blank=True, help_text='logo', null=True, upload_to='producto/'),
        ),
    ]
