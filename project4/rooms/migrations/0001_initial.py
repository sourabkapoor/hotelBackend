# Generated by Django 4.1 on 2022-08-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('availability', models.BooleanField()),
                ('sea_view', models.BooleanField()),
                ('pool_view', models.BooleanField()),
            ],
        ),
    ]