# Generated by Django 5.1.3 on 2025-01-08 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deptapp', '0002_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
