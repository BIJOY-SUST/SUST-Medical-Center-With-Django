# Generated by Django 2.2 on 2019-05-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0010_auto_20190502_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photos',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]