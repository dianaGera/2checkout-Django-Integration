# Generated by Django 3.1 on 2022-02-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_delete_subscription'),
        ('accounts', '0006_auto_20220210_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='active_promotions',
            field=models.ManyToManyField(blank=True, to='checkout.Promotion'),
        ),
    ]
