# Generated by Django 4.0 on 2022-01-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_useraddress_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='zipcode',
            field=models.IntegerField(),
        ),
    ]
