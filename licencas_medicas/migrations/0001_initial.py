# Generated by Django 5.0.1 on 2024-01-20 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Licenca_medica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo', models.CharField(max_length=127)),
                ('data', models.DateField()),
                ('responsavel', models.CharField(max_length=127)),
                ('crm', models.CharField(max_length=127)),
            ],
        ),
    ]
