# Generated by Django 3.0.7 on 2020-06-08 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_dead', '0006_auto_20200607_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thedead',
            name='website',
            field=models.URLField(blank=True, help_text='Add website describing or providing more information about the person.', max_length=255, verbose_name='Website'),
        ),
    ]
