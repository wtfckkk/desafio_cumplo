# Generated by Django 2.1.5 on 2019-01-06 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0002_consulta_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='tipo_consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='indicadores.TipoConsulta'),
        ),
    ]
