# Generated by Django 4.2.2 on 2023-07-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_ticketcart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='previous',
            name='match_unique_name',
        ),
        migrations.RemoveField(
            model_name='ticketcart',
            name='match_unique_name',
        ),
        migrations.AddField(
            model_name='ticketcart',
            name='match_unique_namee',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='upcoming',
            name='match_unique_name',
            field=models.CharField(default='', max_length=120),
        ),
    ]