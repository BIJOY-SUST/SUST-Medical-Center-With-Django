# Generated by Django 2.2 on 2019-06-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0046_medicineinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicineinfo',
            name='medicineafter',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]