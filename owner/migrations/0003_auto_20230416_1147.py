# Generated by Django 2.2.2 on 2023-04-16 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_auto_20230416_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='user_name',
            new_name='owner_name',
        ),
    ]
