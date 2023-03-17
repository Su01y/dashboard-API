# Generated by Django 4.1.7 on 2023-03-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspirant', '0002_remove_aspirant_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aspirant',
            name='education',
            field=models.CharField(choices=[(0, 'high scool'), (1, 'college'), (2, 'bachelor'), (3, 'specialist'), (4, 'master')], default='high scool', max_length=2),
        ),
        migrations.AlterField(
            model_name='aspirant',
            name='rang',
            field=models.CharField(choices=[(0, 'no rang'), (1, 'junior'), (2, 'middle'), (3, 'senior'), (4, 'team lead')], default='no rang', max_length=2),
        ),
    ]