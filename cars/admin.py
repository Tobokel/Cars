from django.contrib import admin
from django import forms
from django.contrib.admin import ModelAdmin

from .models import Region, Category, Car, SubCategory, Like, CarComment

class PersonAdmin(admin.ModelAdmin):
    list_filter = ('id', 'name', 'price', 'steering_wheel')
    list_display = ('id', 'name', 'author', 'price', 'currency', 'region', 'phone_number')
class CarCommentAdmin(admin.ModelAdmin):
    list_filter = ('id', 'name', 'author', 'text')
    list_display = ('id', 'name', 'author', 'text')
class CarSubcategoryAdmin(admin.ModelAdmin):
    list_filter = ('id', 'category', 'name')
    list_display = ('id', 'category', 'name')
class LikeAdmin(admin.ModelAdmin):
    list_filter = ('car', 'rate')
    list_display = ('user', 'car', 'rate', 'like', 'in_bookmarks')
admin.site.register(Region)
admin.site.register(Category)
admin.site.register(SubCategory, CarSubcategoryAdmin)
admin.site.register(CarComment, CarCommentAdmin)
admin.site.register(Car, PersonAdmin)
admin.site.register(Like, LikeAdmin)


