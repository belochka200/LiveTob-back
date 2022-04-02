# Generated by Django 4.0.3 on 2022-04-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_name_popularpeople_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularpeople',
            name='bored',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='popularpeople',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Изображение'),
        ),
    ]