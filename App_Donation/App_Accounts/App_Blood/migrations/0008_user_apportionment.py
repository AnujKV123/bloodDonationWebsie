# Generated by Django 3.1.2 on 2022-03-25 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_Blood', '0007_auto_20220120_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_Apportionment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('gender', models.CharField(max_length=120)),
                ('date_of_birth', models.CharField(max_length=120)),
                ('mobile_no', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('apportionment_date', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('blood_bank_name', models.CharField(max_length=120)),
                ('blood_group', models.CharField(max_length=120)),
                ('g_id', models.CharField(max_length=120)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]