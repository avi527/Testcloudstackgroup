# Generated by Django 3.0.7 on 2020-06-06 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(default=False, max_length=30)),
                ('Last_Name', models.CharField(default=False, max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(default=False, max_length=30)),
                ('Profile_Image', models.CharField(default=False, max_length=30)),
            ],
        ),
    ]