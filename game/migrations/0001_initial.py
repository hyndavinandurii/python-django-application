# Generated by Django 5.0.7 on 2024-07-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.JSONField(default=list)),
                ('current_player', models.CharField(max_length=1)),
            ],
        ),
    ]
