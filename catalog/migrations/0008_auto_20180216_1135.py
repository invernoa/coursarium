# Generated by Django 2.0.2 on 2018-02-16 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20180215_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='short_description',
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(blank=True, default=None, max_length=28, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Category'),
        ),
    ]
