# Generated by Django 3.2.7 on 2021-09-29 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Accounts', '0004_auto_20210929_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bloodgroup',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], max_length=20, null=True),
        ),
    ]