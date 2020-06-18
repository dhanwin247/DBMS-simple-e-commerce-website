# Generated by Django 3.0.7 on 2020-06-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_purchase_purchaseproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]