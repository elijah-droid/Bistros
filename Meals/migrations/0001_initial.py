# Generated by Django 4.2.7 on 2023-12-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Dishes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch')], max_length=100)),
                ('Dishes', models.ManyToManyField(to='Dishes.dish')),
            ],
        ),
    ]
