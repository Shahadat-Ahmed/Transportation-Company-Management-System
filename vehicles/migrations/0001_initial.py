# Generated by Django 2.2.2 on 2023-04-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vehicle_license_plate', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('Vehicle_id', models.TextField(blank=True, null=True)),
                ('fitness', models.TextField(blank=True, null=True)),
                ('Vehicle_company', models.CharField(blank=True, max_length=60, null=True)),
                ('Vehicle_colour', models.CharField(blank=True, max_length=60, null=True)),
                ('Vehicle_model_year', models.CharField(blank=True, max_length=60, null=True)),
                ('Vehicle_type', models.CharField(blank=True, max_length=20, null=True)),
                ('Vehicle_capacity', models.IntegerField(blank=True, null=True)),
                ('Vehicle_milage', models.CharField(blank=True, max_length=10, null=True)),
                ('Vehicle_speed', models.CharField(blank=True, max_length=20, null=True)),
                ('Vehicle_tonage', models.CharField(blank=True, max_length=20, null=True)),
                ('Vehicle_total_axis', models.CharField(blank=True, max_length=20, null=True)),
                ('Vehicle_uploaded_by', models.CharField(blank=True, max_length=100, null=True)),
                ('isGeared', models.TextField(blank=True, null=True)),
                ('Vehicle_description', models.CharField(blank=True, max_length=1500, null=True)),
                ('Vehicle_price', models.IntegerField(blank=True, null=True)),
                ('is_anonymous', models.BooleanField(blank=True, default=False, null=True)),
                ('is_authenticated', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
    ]
