# Generated by Django 2.2.6 on 2019-10-24 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('verwaltung', '0003_auto_20191024_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='teilnahme',
            name='schuljahr',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='verwaltung.Schuljahr'),
        ),
    ]
