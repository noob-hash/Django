# Generated by Django 4.1 on 2023-02-18 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='updatedDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
