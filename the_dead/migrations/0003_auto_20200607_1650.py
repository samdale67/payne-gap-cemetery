# Generated by Django 3.0.7 on 2020-06-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_dead', '0002_auto_20200607_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='thedead',
            name='nick_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='thedead',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='thedead',
            name='maiden_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Maiden Name'),
        ),
    ]