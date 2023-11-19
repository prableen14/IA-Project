# Generated by Django 4.2.7 on 2023-11-18 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoApp', '0003_coin_icon_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialsProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follows', models.ManyToManyField(blank=True, related_name='followed_by', to='cryptoApp.socialsprofile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
