# Generated by Django 3.2 on 2023-05-13 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_auto_20230512_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='status',
            field=models.TextField(blank=True, null=True),
        ),
    ]
