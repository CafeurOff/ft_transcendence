# Generated by Django 4.2.3 on 2024-05-14 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singlepage', '0011_remove_tournament_winner_uid_tournament_winner_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='score_player1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='score_player2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='in_game',
            field=models.BooleanField(default=False),
        ),
    ]