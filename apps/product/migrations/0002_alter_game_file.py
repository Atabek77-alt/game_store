# Generated by Django 5.1.6 on 2025-03-07 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='over_all/files/'),
        ),
    ]
