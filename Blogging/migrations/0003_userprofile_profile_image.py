# Generated by Django 3.0.6 on 2020-05-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogging', '0002_auto_20200507_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
