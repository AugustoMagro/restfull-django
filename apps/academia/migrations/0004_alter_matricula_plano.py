# Generated by Django 5.1.1 on 2024-09-12 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0003_matricula_plano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='plano',
            field=models.CharField(choices=[('A', 'Mensal'), ('B', 'Semestral'), ('C', 'Anual')], default='A', max_length=10),
        ),
    ]
