# Generated by Django 4.1.3 on 2022-11-02 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_delete_orderdetails_delete_orders'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
