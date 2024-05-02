# Generated by Django 4.2.3 on 2024-05-02 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('singlepage', '0009_tournament_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='winner_uid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tournament_winner', to=settings.AUTH_USER_MODEL),
        ),
    ]