
from django.db import models

# Create your models here.
from account.models import User


class Region(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'region'

    def __str__(self):
        return f'{self.id}, {self.name}'

class Category(models.Model):
    name = models.CharField(max_length=128)
    icon = models.ImageField(upload_to='cars_icons/')

    class Meta:
        db_table = 'category'

    def __str__(self):
        return f'{self.id}, {self.name}'

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='cars_models/')
    from_year = models.IntegerField()
    to_year = models.IntegerField()

    class Meta:
        db_table = 'sub_category'

    def __str__(self):
        return f'{self.category}, {self.name}'


class Car(models.Model):
    STEERING_WHEEL = {
        ('right', 'Правый'),
        ('left', 'Левый')
    }
    VALUTA = {
        ('usd', 'usd'),
        ('som', 'сом')
    }

    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    steering_wheel = models.CharField(max_length=24, choices=STEERING_WHEEL, default='left')
    region = models.ForeignKey(Region,  on_delete=models.CASCADE, related_name='region')
    body = models.TextField()
    currency = models.CharField(max_length=24, choices=VALUTA, default='usd')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars_image', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    class Meta:
        db_table = 'car'

    def __str__(self):
        return f'{self.id}, {self.name}, {self.author}, {self.price}, {self.currency}, {self.region}, {self.phone_number}'

class CarComment(models.Model):
    name = models.ForeignKey(Car,
                                on_delete=models.CASCADE,
                                related_name='comments')

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.author}, {self.text}, от {self.created_at.strftime("%d-%m-%Y %H:%M")}'

class Like(models.Model):
    RATE_CHOICES = (
        (1, 'Нормальная машина'),
        (2, 'Хорошая машина'),
        (3, 'Отличная машина'),
        (4, 'Классная машина'),
        (5, 'Машина ОГОНЬ!')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name='likes', on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    def __str__(self):
        return f'{self.car}, rating:{self.rate}'







