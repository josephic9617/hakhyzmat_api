# Generated by Django 5.0.6 on 2024-09-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_service_name_servicedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('company_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]
