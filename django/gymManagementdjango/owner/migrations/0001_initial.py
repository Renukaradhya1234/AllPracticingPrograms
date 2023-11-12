# Generated by Django 4.2.3 on 2023-08-24 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerDetails',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=50)),
                ('tdob', models.DateField()),
                ('tgender', models.CharField(max_length=10)),
                ('temail', models.EmailField(max_length=254, unique=True)),
                ('tphone', models.CharField(max_length=10, unique=True)),
                ('tusername', models.CharField(max_length=50)),
                ('tpassword', models.CharField(max_length=20)),
                ('timage', models.ImageField(upload_to='images')),
            ],
            options={
                'db_table': 'trainerdetails',
            },
        ),
    ]