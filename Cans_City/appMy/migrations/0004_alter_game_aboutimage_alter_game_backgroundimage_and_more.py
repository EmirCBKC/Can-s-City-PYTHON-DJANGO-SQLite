# Generated by Django 4.2.4 on 2023-09-10 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0003_game_editionimage_alter_game_iframe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='aboutImage',
            field=models.ImageField(blank=True, null=True, upload_to='background_images/', verbose_name='About Image'),
        ),
        migrations.AlterField(
            model_name='game',
            name='backgroundImage',
            field=models.ImageField(blank=True, null=True, upload_to='background_images/', verbose_name='Background Image'),
        ),
        migrations.AlterField(
            model_name='game',
            name='editionImage',
            field=models.ImageField(blank=True, null=True, upload_to='background_images/', verbose_name='Edition Image'),
        ),
        migrations.AlterField(
            model_name='game',
            name='leftPng',
            field=models.ImageField(blank=True, null=True, upload_to='background_images/', verbose_name='Left Png'),
        ),
        migrations.AlterField(
            model_name='game',
            name='rightPng',
            field=models.ImageField(blank=True, null=True, upload_to='background_images/', verbose_name='Right Png'),
        ),
    ]
