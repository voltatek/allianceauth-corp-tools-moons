# Generated by Django 3.2.5 on 2021-08-22 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corptools', '0058_auto_20210808_0635'),
        ('moons', '0005_remove_miningobservation_frack'),
    ]

    operations = [
        migrations.AddField(
            model_name='miningobservation',
            name='structure',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='corptools.evelocation'),
        ),
    ]
