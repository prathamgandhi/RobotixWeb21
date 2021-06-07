# Generated by Django 3.2 on 2021-05-29 02:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='DIY_FYI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='extras/diy_fyi/img')),
                ('mentor', models.CharField(max_length=50)),
                ('members', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=8)),
                ('link', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='DIY',
        ),
        migrations.DeleteModel(
            name='FYI',
        ),
    ]