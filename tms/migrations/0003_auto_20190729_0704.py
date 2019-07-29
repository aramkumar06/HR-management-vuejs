# Generated by Django 2.1.2 on 2019-07-29 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0002_auto_20190724_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='earning',
            name='week_of_year',
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('Calculated', 'Calculated'), ('Active', 'Active')], help_text='active or calculated', max_length=20),
        ),
        migrations.AlterField(
            model_name='earning',
            name='status',
            field=models.CharField(choices=[('Withdraw', 'Withdraw')], default='Withdraw', max_length=20),
        ),
    ]
