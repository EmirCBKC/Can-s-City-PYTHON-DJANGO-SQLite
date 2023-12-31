# Generated by Django 4.2.4 on 2023-09-12 14:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMy', '0006_alter_profil_profileimg_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='likes',
            field=models.ManyToManyField(related_name='liked_games', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='game',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
