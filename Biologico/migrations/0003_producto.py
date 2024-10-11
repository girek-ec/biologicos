# Generated by Django 4.0.6 on 2024-10-02 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biologico', '0002_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(blank=True, help_text='slider  1600x964', null=True, upload_to='slider/')),
                ('link_video', models.CharField(blank=True, help_text='Link youtube', max_length=200, null=True)),
                ('titulo', models.CharField(blank=True, max_length=90, null=True)),
                ('sub_titulo', models.CharField(blank=True, max_length=90, null=True)),
                ('detalle', models.TextField(blank=True, max_length=400, null=True)),
            ],
            options={
                'verbose_name_plural': '2. Slider ',
            },
        ),
    ]
