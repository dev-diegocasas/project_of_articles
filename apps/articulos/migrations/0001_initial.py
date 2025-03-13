# Generated by Django 5.1.7 on 2025-03-12 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('resumen', models.TextField()),
                ('detalle', models.TextField()),
                ('foto', models.ImageField(upload_to='noticias/')),
                ('publicada', models.BooleanField(default=True)),
            ],
        ),
    ]
