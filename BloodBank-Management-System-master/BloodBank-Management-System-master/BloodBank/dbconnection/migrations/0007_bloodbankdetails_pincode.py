# Generated by Django 2.1.5 on 2019-04-06 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbconnection', '0006_auto_20190406_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodbankdetails',
            name='pincode',
            field=models.CharField(default='', max_length=10),
        ),
    ]
