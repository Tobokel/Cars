# Generated by Django 3.2.7 on 2021-09-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='currency',
            field=models.CharField(choices=[('usd', 'usd'), ('som', 'сом')], default='usd', max_length=24),
        ),
    ]
