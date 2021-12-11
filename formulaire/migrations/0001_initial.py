# Generated by Django 3.2.9 on 2021-12-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/')),
                ('first_name', models.CharField(max_length=100)),
                ('family_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]