# Generated by Django 5.0.3 on 2024-04-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pdf_contenido_pdf_fundamentacion_pdf_metodologia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='bibliografia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pdf',
            name='evaluacion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
