# Generated by Django 3.2.7 on 2021-10-04 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20211004_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePhotos',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.user')),
                ('profilephoto', models.ImageField(blank=True, default='default.png', null=True, upload_to='usersphotos/')),
            ],
        ),
    ]