# Generated by Django 4.1.7 on 2023-03-26 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_menu_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='BookingDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
