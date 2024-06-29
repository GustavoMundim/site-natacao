# Generated by Django 5.0.2 on 2024-04-02 03:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitenatacao', '0003_rename_inscricao_inscrito'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='fotos')),
                ('descricao', models.CharField(max_length=100)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]