# Generated by Django 2.1.7 on 2020-03-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0003_recruitment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='intention_reason',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='priority_reason',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='task_completion_reason',
            field=models.TextField(max_length=1000),
        ),
    ]