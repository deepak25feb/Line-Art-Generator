# Generated by Django 3.2.7 on 2021-10-03 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20211003_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convertedphotos',
            name='id',
        ),
        migrations.AlterField(
            model_name='convertedphotos',
            name='photooriginal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.photos'),
        ),
    ]
