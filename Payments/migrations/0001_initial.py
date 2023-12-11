# Generated by Django 4.2.7 on 2023-12-09 18:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField()),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Failed', 'Failed'), ('Success', 'Success')], max_length=100)),
            ],
        ),
    ]