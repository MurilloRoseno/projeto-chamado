# Generated by Django 2.2.7 on 2019-11-22 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Setor')),
                ('tipo', models.TextField(choices=[('A', 'Administrativo'), ('O', 'Operacional'), ('T', 'Terceirizado')], verbose_name='Tipo de Setor')),
                ('contato', models.CharField(max_length=9, verbose_name='Ramal')),
            ],
        ),
    ]
