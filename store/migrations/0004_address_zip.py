# Generated by Django 4.2.1 on 2023-07-11 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
