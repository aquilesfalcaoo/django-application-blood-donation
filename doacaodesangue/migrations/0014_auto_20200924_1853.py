# Generated by Django 3.1.1 on 2020-09-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacaodesangue', '0013_auto_20200924_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doador',
            name='RG',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='medico',
            name='CRM',
            field=models.IntegerField(),
        ),
    ]