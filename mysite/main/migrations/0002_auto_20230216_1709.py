# Generated by Django 3.2.12 on 2023-02-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aplikacija',
            name='aplikacija_slika1',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='aplikacija',
            name='aplikacija_slika2',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='aplikacija',
            name='aplikacija_slika3',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='aplikacija',
            name='aplikacija_slika4',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='aplikacija',
            name='aplikacija_URL',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='aplikacija',
            name='aplikacija_slika',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
