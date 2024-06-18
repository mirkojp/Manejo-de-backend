# Generated by Django 5.0.3 on 2024-06-17 00:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BattleFaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outcome', models.CharField(blank=True, max_length=100)),
                ('battle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warhammer_api.battle')),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warhammer_api.faction')),
            ],
        ),
        migrations.AddField(
            model_name='battle',
            name='factions',
            field=models.ManyToManyField(through='warhammer_api.BattleFaction', to='warhammer_api.faction'),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unit_type', models.CharField(max_length=100)),
                ('strength', models.IntegerField()),
                ('description', models.TextField()),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='warhammer_api.faction')),
            ],
        ),
    ]
