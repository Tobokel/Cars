# Generated by Django 3.2.7 on 2021-09-12 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20210912_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='car',
            name='currency',
            field=models.CharField(choices=[('som', 'сом'), ('usd', 'usd')], default='usd', max_length=24),
        ),
        migrations.AlterField(
            model_name='car',
            name='steering_wheel',
            field=models.CharField(choices=[('right', 'Правый'), ('left', 'Левый')], default='left', max_length=24),
        ),
    ]
