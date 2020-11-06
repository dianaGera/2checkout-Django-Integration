# Generated by Django 3.1 on 2020-11-04 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20201104_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='promotion_percent',
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion_fixed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.promotion_fixed')),
                ('promotion_percent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.promotion_percent')),
            ],
        ),
        migrations.AlterField(
            model_name='subscription',
            name='promotion_fixed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.promotion'),
        ),
    ]
