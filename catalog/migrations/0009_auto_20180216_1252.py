# Generated by Django 2.0.2 on 2018-02-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20180216_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='summary',
            field=models.TextField(max_length=1000),
        ),
    ]
