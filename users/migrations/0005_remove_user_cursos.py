# Generated by Django 5.0.1 on 2024-04-10 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_create_first_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cursos',
        ),
    ]
