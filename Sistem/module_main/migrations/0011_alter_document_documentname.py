# Generated by Django 4.0.3 on 2022-04-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_main', '0010_document_documentlength'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='documentName',
            field=models.CharField(max_length=30),
        ),
    ]
