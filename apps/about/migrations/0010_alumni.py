# Generated by Django 3.2 on 2021-12-08 19:18

import about.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_alter_team_post_assign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to=about.models.PathAndRename('about/team/'))),
                ('name', models.CharField(max_length=250, null=True)),
                ('branch', models.CharField(max_length=250, null=True)),
                ('domain_assign', models.CharField(choices=[('WA', 'WEB & APP'), ('PM', 'PR MARKETING'), ('DO', 'DOCUMENTATION'), ('SS', 'SPONSERSHIP'), ('DV', 'DESIGN'), ('TT', 'TECHNICAL')], max_length=2, null=True)),
                ('fb_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('github_url', models.URLField(blank=True, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('joining', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]
