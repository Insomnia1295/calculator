# Generated by Django 4.2.3 on 2023-08-07 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number1', models.FloatField()),
                ('number2', models.FloatField()),
            ],
        ),
    ]
