# Generated by Django 5.0.6 on 2024-09-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_banner_brand_icon_service_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service',
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category name')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories/')),
                ('sub_categories', models.ManyToManyField(blank=True, null=True, related_name='sub_categories', to='main.category', verbose_name='Sub categories')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='categories', to='main.category', verbose_name='Categories'),
        ),
    ]
