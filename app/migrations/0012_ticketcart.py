# Generated by Django 4.2.2 on 2023-07-28 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_previous_regteam_preferred_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticketcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_unique_name', models.CharField(default='', max_length=120)),
                ('match_tickets_quantity', models.IntegerField(default=1)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
