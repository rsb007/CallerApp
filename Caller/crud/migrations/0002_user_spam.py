# Generated by Django 2.2.1 on 2019-05-04 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='spam',
            field=models.BooleanField(default=False),
        ),
    ]