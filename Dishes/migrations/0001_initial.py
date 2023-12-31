# Generated by Django 4.2.7 on 2023-12-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='Images/Dishes')),
                ('Description', models.TextField(max_length=10000)),
                ('Foods', models.ManyToManyField(to='Food.food')),
            ],
        ),
    ]
