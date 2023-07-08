# Generated by Django 3.0.5 on 2023-03-06 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0034_auto_20230305_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='prescription',
            field=models.CharField(default='Not Treated', max_length=500),
        ),
        migrations.AlterField(
            model_name='patient',
            name='tests',
            field=models.CharField(default='Not Treated', max_length=100),
        ),
    ]
