# Generated by Django 2.2.5 on 2019-10-02 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0003_auto_20191002_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='parent',
        ),
    ]