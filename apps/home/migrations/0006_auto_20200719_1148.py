# Generated by Django 3.0.8 on 2020-07-19 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200719_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='facebook',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='instagram',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='linkedln',
            field=models.CharField(default='', max_length=60),
        ),
    ]
