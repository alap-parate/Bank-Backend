# Generated by Django 5.0.7 on 2024-07-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary_master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='code',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]