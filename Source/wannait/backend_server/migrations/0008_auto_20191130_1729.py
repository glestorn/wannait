# Generated by Django 2.2.5 on 2019-11-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_server', '0007_backendproduct_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backendproduct',
            name='origin',
            field=models.CharField(max_length=1000),
        ),
    ]
