# Generated by Django 3.0.7 on 2020-06-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_dead', '0004_auto_20200607_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='thedead',
            name='grave_location',
            field=models.CharField(default='', max_length=255, verbose_name='Grave Location'),
        ),
    ]
