# Generated by Django 4.1.2 on 2023-06-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ename', models.CharField(max_length=100)),
                ('Eid', models.IntegerField()),
                ('Edept', models.CharField(max_length=100)),
            ],
        ),
    ]
