# Generated by Django 2.1.2 on 2019-07-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(help_text='Phone number related to this account.It could be null', max_length=14, null=True),
        ),
    ]
