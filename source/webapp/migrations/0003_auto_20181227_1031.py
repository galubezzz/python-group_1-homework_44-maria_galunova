# Generated by Django 2.1 on 2018-12-27 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20181223_2124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('can_take_and_deliver_orders', 'Может брать и доставлять заказы')]},
        ),
    ]