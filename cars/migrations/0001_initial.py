# Generated by Django 4.2 on 2023-07-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('1', 'Autos'), ('2', 'Pickups y Comerciales'), ('3', 'SUVs y Crossovers')], default='1', max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='car_images')),
            ],
        ),
    ]