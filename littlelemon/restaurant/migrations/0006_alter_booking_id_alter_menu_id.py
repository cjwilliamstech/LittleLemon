# Generated by Django 4.1.7 on 2023-03-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_rename_id_booking_id_rename_id_menu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
