# Generated by Django 2.2.6 on 2019-10-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verwaltung', '0002_schuljahr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schuljahr',
            name='schuljahr',
            field=models.CharField(max_length=7, verbose_name='Schuljahr'),
        ),
    ]