# Generated by Django 4.2.16 on 2024-10-08 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biologico', '0018_edit_pag_imag_fondo_02_edit_pag_imag_fondo_03_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='edit_pag',
            name='ico_bene1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='ico_bene2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='ico_bene3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='ico_bene4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='ico_subti1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='ico_subti2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='ico_subti3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='ico_subti4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='ico_titulo1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='ico_titulo2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='ico_titulo3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='edit_pag',
            name='ico_titulo4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]