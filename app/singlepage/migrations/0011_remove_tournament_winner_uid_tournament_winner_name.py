# Generated by Django 4.2.3 on 2024-05-09 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singlepage', '0010_alter_tournament_winner_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='winner_uid',
        ),
        migrations.AddField(
            model_name='tournament',
            name='winner_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]