# Generated by Django 5.0.6 on 2024-09-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_category_sub_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub_categories',
            field=models.ManyToManyField(blank=True, to='main.category'),
        ),
        migrations.AlterField(
            model_name='service',
            name='categories',
            field=models.ManyToManyField(blank=True, to='main.category'),
        ),
    ]
