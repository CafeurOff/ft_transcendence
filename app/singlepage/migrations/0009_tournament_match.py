# Generated by Django 4.2.3 on 2024-04-29 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('singlepage', '0008_remove_tournament_current_match_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament_Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField(blank=True, default=0)),
                ('round_id', models.IntegerField(blank=True, default=0)),
                ('player1', models.CharField(blank=True, max_length=100)),
                ('player2', models.CharField(blank=True, max_length=100)),
                ('winner', models.CharField(blank=True, max_length=100)),
                ('tournament_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament', to='singlepage.tournament')),
            ],
        ),
    ]