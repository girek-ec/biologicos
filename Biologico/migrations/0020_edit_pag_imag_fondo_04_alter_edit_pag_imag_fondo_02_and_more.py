# Generated by Django 4.2.16 on 2024-10-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biologico', '0019_edit_pag_ico_bene1_edit_pag_ico_bene2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='edit_pag',
            name='imag_fondo_04',
            field=models.FileField(blank=True, help_text='fondo  1894x718', null=True, upload_to='slider/'),
        ),
        migrations.AlterField(
            model_name='edit_pag',
            name='imag_fondo_02',
            field=models.FileField(blank=True, help_text='fondo   1894x718', null=True, upload_to='slider/'),
        ),
        migrations.AlterField(
            model_name='edit_pag',
            name='imag_fondo_03',
            field=models.FileField(blank=True, help_text='fondo  1894x718', null=True, upload_to='slider/'),
        ),
        migrations.AlterField(
            model_name='edit_pag',
            name='imag_pie',
            field=models.FileField(blank=True, help_text='fondo  1894x718', null=True, upload_to='slider/'),
        ),
    ]
