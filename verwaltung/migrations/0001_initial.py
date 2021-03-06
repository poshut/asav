# Generated by Django 2.2 on 2019-10-23 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aktivitaet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Aktivität',
                'verbose_name_plural': 'Aktivitäten',
            },
        ),
        migrations.CreateModel(
            name='AktivitaetErgebnis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mint_punkte', models.IntegerField(verbose_name='MINT-EC-Punkte')),
                ('aktivitaet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='verwaltung.Aktivitaet', verbose_name='Aktivität')),
            ],
            options={
                'verbose_name': 'Aktivitätsergebnis',
                'verbose_name_plural': 'Aktivitätsergebnisse',
            },
        ),
        migrations.CreateModel(
            name='Ergebnis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Ergebnis',
                'verbose_name_plural': 'Ergebnisse',
            },
        ),
        migrations.CreateModel(
            name='Fach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('kuerzel', models.CharField(max_length=10, verbose_name='Kürzel')),
            ],
            options={
                'verbose_name': 'Fach',
                'verbose_name_plural': 'Fächer',
            },
        ),
        migrations.CreateModel(
            name='Klasse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Klassen',
            },
        ),
        migrations.CreateModel(
            name='Lehrer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Titel')),
                ('vname', models.CharField(max_length=30, verbose_name='Vorname')),
                ('nname', models.CharField(max_length=30, verbose_name='Nachname')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('kuerzel', models.CharField(max_length=10, verbose_name='Kürzel')),
            ],
            options={
                'verbose_name': 'Lehrer',
                'verbose_name_plural': 'Lehrer',
            },
        ),
        migrations.CreateModel(
            name='Schueler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vname', models.CharField(max_length=30, verbose_name='Vorname')),
                ('nname', models.CharField(max_length=30, verbose_name='Nachname')),
                ('email', models.EmailField(max_length=254)),
                ('klasse', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='verwaltung.Klasse')),
            ],
            options={
                'verbose_name': 'Schüler',
                'verbose_name_plural': 'Schüler',
            },
        ),
        migrations.CreateModel(
            name='Teilnahme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aktivitaetergebnis', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='verwaltung.AktivitaetErgebnis', verbose_name='Aktivitätsergebnis')),
                ('lehrer1', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lehrer1_set', to='verwaltung.Lehrer', verbose_name='1. Betreuender Lehrer')),
                ('lehrer2', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lehrer2_set', to='verwaltung.Lehrer', verbose_name='2. Betreuender Lehrer')),
                ('schueler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teilnahmen', to='verwaltung.Schueler', verbose_name='Schüler')),
            ],
            options={
                'verbose_name': 'Teilnahme',
                'verbose_name_plural': 'Teilnahmen',
            },
        ),
        migrations.AddField(
            model_name='aktivitaetergebnis',
            name='ergebnis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='verwaltung.Ergebnis'),
        ),
        migrations.AddField(
            model_name='aktivitaet',
            name='fach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='verwaltung.Fach'),
        ),
    ]
