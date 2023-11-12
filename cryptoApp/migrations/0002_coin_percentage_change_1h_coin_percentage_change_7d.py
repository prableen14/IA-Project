# Generated by Django 4.2.7 on 2023-11-11 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='percentage_change_1h',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='coin',
            name='percentage_change_7d',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
