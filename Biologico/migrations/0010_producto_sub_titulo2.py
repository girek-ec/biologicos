# Generated by Django 4.2.16 on 2024-10-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biologico', '0009_blog_producto_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='sub_titulo2',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
    ]
