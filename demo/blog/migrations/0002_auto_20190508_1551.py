# Generated by Django 2.2.1 on 2019-05-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloginnerpage',
            options={'verbose_name': 'Blog inner page'},
        ),
        migrations.AlterModelOptions(
            name='blogpage',
            options={'verbose_name': 'Blog page'},
        ),
        migrations.AddField(
            model_name='bloginnerpage',
            name='date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='bloginnerpage',
            name='email',
            field=models.EmailField(max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='bloginnerpage',
            name='is_important',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
