# Generated by Django 4.2.3 on 2023-07-21 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais_para_adocao', '0010_anuncioanimal_id_zona_do_pais_fk'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedidasParaAjudar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medida', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Medidas para Ajudar',
            },
        ),
    ]