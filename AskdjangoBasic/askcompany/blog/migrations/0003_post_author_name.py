# Generated by Django 2.2.24 on 2021-07-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_name',
            field=models.CharField(default='anonymous', max_length=20),
            preserve_default=False,
        ),
    ]
