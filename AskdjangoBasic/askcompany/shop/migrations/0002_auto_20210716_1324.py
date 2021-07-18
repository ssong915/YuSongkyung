# Generated by Django 2.2.24 on 2021-07-16 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_publish',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(default=''),
        ),
    ]