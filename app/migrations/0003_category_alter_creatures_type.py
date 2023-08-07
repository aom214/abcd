# Generated by Django 4.2.2 on 2023-06-28 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_creatures_image_creatures_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=80)),
            ],
        ),
        migrations.AlterField(
            model_name='creatures',
            name='type',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]