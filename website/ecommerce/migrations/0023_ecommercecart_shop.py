# Generated by Django 4.2 on 2023-05-30 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0022_shop_paypal'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecommercecart',
            name='shop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='ecommerce.shop'),
            preserve_default=False,
        ),
    ]
