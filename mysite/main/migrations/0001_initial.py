# Generated by Django 4.0.6 on 2023-02-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_ime', models.CharField(max_length=50)),
                ('student_prezime', models.CharField(max_length=50)),
                ('student_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Aplikacija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aplikacija_naziv', models.CharField(max_length=100)),
                ('aplikacija_opis', models.TextField()),
                ('aplikacija_datum', models.DateField()),
                ('aplikacija_URL', models.URLField()),
                ('aplikacija_AkGod', models.CharField(max_length=30)),
                ('aplikacija_slika', models.ImageField(blank=True, null=True, upload_to='')),
                ('aplikacija_student', models.ManyToManyField(to='main.student')),
            ],
        ),
    ]
