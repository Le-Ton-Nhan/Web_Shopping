# Generated by Django 4.1.3 on 2022-11-02 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderDetails',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
