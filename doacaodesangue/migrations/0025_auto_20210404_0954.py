# Generated by Django 3.1.7 on 2021-04-04 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacaodesangue', '0024_auto_20210403_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doador',
            name='CPF',
            field=models.CharField(default='', max_length=14),
        ),
    ]