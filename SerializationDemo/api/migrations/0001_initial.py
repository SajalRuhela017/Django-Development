# Generated by Django 4.2.2 on 2023-07-04 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=25)),
            ],
        ),
    ]