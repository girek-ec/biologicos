# Generated by Django 4.0.6 on 2024-10-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biologico', '0024_alter_edit_pag_mision_alter_edit_pag_vision'),
    ]

    operations = [
        migrations.AddField(
            model_name='edit_pag',
            name='about_destacado_01',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='about_destacado_02',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='about_destacado_03',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='about_destacado_04',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]