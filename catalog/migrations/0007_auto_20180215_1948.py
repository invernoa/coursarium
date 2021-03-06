# Generated by Django 2.0.2 on 2018-02-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20180214_1946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'Media', 'verbose_name_plural': 'Media'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Statuses'},
        ),
        migrations.AddField(
            model_name='course',
            name='short_description',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
