# Generated by Django 4.0 on 2022-01-05 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productimage_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image',
            new_name='sub_image',
        ),
        migrations.AddField(
            model_name='products',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
