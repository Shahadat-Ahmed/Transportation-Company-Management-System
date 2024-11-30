# Generated by Django 2.2.2 on 2023-04-16 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('owner_name', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255, unique=True)),
                ('NID', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone1', models.CharField(max_length=255)),
                ('phone2', models.CharField(blank=True, max_length=255, null=True)),
                ('phone3', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.TextField()),
                ('share', models.IntegerField()),
                ('address', models.TextField()),
                ('is_admin', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
