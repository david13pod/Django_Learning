# Generated by Django 3.1.6 on 2021-02-16 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=264, unique=True)),
                ('lastname', models.CharField(max_length=264, unique=True)),
                ('email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
    ]
