# Generated by Django 5.0 on 2023-12-17 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('contenido', models.CharField(max_length=1450, verbose_name='Contenido')),
                ('visible', models.BooleanField(default=True)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('imagen', models.ImageField(upload_to='blog/imagenes/')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaArticulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.articulo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('CategoriaArticulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoriaarticulo')),
            ],
        ),
    ]
