# Generated by Django 4.0.6 on 2024-12-17 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biologico', '0044_servicio_beneficio_5_servicio_beneficio_6'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='beneficio_parrafo',
            new_name='beneficio_parrafo_1',
        ),
        migrations.AddField(
            model_name='servicio',
            name='beneficio_parrafo_2',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]