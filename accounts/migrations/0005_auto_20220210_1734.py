# Generated by Django 3.1 on 2022-02-10 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_myuser_total_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='total_payment',
            field=models.FloatField(default=0),
        ),
    ]
