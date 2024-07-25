# Generated by Django 5.0.7 on 2024-07-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='role',
            field=models.CharField(choices=[('superadmin', 'Super Admin'), ('admin', 'Admin'), ('employee', 'Employee')], default='employee', max_length=10),
        ),
    ]