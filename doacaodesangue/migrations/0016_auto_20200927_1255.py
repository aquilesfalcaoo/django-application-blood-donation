# Generated by Django 3.1.1 on 2020-09-27 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacaodesangue', '0015_medico_especialidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='especialidade',
            field=models.CharField(choices=[('1', 'Hematologista'), ('2', 'Enfermeiro'), ('3', 'Outro')], default='', max_length=12),
        ),
    ]