# Generated by Django 3.2.7 on 2021-09-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='currency',
            field=models.CharField(choices=[('som', 'сом'), ('usd', 'usd')], default='usd', max_length=24),
        ),
        migrations.AlterField(
            model_name='car',
            name='steering_wheel',
            field=models.CharField(choices=[('left', 'Левый'), ('right', 'Правый')], default='left', max_length=24),
        ),
        migrations.AlterField(
            model_name='carcomment',
            name='rating',
            field=models.SmallIntegerField(blank=True, default=1),
        ),
    ]
