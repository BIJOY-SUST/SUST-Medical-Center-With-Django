# Generated by Django 2.2 on 2019-04-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='height',
            field=models.FloatField(blank=True),
        ),
    ]