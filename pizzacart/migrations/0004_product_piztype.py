# Generated by Django 3.2.6 on 2021-10-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzacart', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='piztype',
            field=models.CharField(choices=[('NV', 'NON-VEG'), ('V', 'VEG')], default='', max_length=25),
        ),
    ]
