# Generated by Django 4.2 on 2024-04-05 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DynamoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleorigin',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
