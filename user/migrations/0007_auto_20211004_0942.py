# Generated by Django 3.2.7 on 2021-10-04 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20211003_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='imageconverted',
            field=models.ImageField(blank=True, null=True, upload_to='converted/'),
        ),
        migrations.DeleteModel(
            name='ConvertedPhotos',
        ),
    ]