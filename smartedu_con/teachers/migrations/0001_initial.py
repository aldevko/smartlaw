# Generated by Django 4.0.4 on 2022-04-16 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='courses/%Y/%m/%d')),
                ('facebook', models.URLField(blank=True, max_length=100)),
                ('twitter', models.URLField(blank=True, max_length=100)),
                ('linkedin', models.URLField(blank=True, max_length=100)),
                ('youtube', models.URLField(blank=True, max_length=100)),
            ],
        ),
    ]
