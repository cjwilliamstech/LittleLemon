# Generated by Django 4.1.7 on 2023-03-26 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_alter_booking_id_alter_menu_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='ID',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='ID',
            new_name='id',
        ),
    ]
