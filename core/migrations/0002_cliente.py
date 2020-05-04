# Generated by Django 3.0.5 on 2020-04-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=15, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=15, verbose_name='Sobrenome')),
                ('email', models.CharField(max_length=30, verbose_name='E-mail')),
            ],
        ),
    ]
