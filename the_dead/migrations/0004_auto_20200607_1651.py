# Generated by Django 3.0.7 on 2020-06-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_dead', '0003_auto_20200607_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thedead',
            name='nick_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nick Name'),
        ),
    ]
