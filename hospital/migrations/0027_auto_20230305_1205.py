# Generated by Django 3.0.5 on 2023-03-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0026_auto_20230305_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='tests',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
