# Generated by Django 3.1.1 on 2020-09-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=100)),
                ('tipo_sanguineo', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_medico', models.CharField(max_length=100)),
                ('crm', models.CharField(max_length=100)),
            ],
        ),
    ]