# Generated by Django 4.2.2 on 2023-07-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_regteam_alter_register_players_team_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='previous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=30)),
                ('team2', models.CharField(max_length=30)),
                ('match_unique_name', models.CharField(default='', max_length=120)),
                ('match_won_team', models.CharField(max_length=100)),
                ('match_venue', models.CharField(default='', max_length=50)),
                ('match_date', models.DateField()),
                ('match_time', models.TimeField()),
                ('match_desc', models.TextField()),
                ('match_image', models.ImageField(default='', upload_to='game/images')),
            ],
        ),
        migrations.AddField(
            model_name='regteam',
            name='preferred_location',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='upcoming',
            name='match_price',
            field=models.IntegerField(default=0),
        ),
    ]
