# Generated by Django 4.2.3 on 2023-07-20 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animais_para_adocao', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cordopelo',
            old_name='porte_tamanho',
            new_name='cor_do_pelo',
        ),
    ]
