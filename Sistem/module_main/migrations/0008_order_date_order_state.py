# Generated by Django 4.0.3 on 2022-04-03 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_main', '0007_rename_orderby_order_orderid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.CharField(default='00:00', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.IntegerField(default=0, null=True),
        ),
    ]