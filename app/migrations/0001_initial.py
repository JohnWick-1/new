# Generated by Django 2.1 on 2019-08-22 03:56

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=33)),
                ('last_name', models.CharField(max_length=33)),
                ('marks', models.IntegerField()),
                ('DOB', models.DateField()),
            ],
            options={
                'db_table': 'student',
            },
            managers=[
                ('objs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Student2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=33)),
                ('last_name', models.CharField(max_length=33)),
                ('marks', models.IntegerField()),
                ('DOB', models.DateField()),
            ],
            options={
                'db_table': 'student2',
            },
        ),
    ]
