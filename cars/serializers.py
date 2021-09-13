from rest_framework import serializers

from cars.models import Car, SubCategory, Category, Region, CarComment, Like


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = '__all__'

class CarCommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CarComment
        fields = '__all__'

    # def validate_comment(self, car):
    #     request = self.context.get('request')
    #     user = request.user
    #
    #     if self.Meta.model.objects.filter(car=car, author=user).exists():
    #         raise serializers.ValidationError('Вы уже комментировали данную статью.')
    #     return car

    # def validate_rating(self, rating):
    #     if rating not in range(1, 11):
    #         raise serializers.ValidationError('Рейтинг может быть от 1 до 10')
    #     return rating

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'



class CarSerializer(serializers.ModelSerializer):
    comments = CarCommentSerializer(many=True)
    likes = LikeSerializer(many=True)
    sub_category = SubCategorySerializer(read_only=True)
    region = RegionSerializer(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.likes.filter(like=True).count()
        return representation
    class Meta:
        model = Car

        fields = '__all__'



class CreateCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'
    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError('Цена не должна быть отрицательной')
        return price

class CarDetailsSerializer(serializers.ModelSerializer):
    comments = CarCommentSerializer(many=True)
    sub_category = SubCategorySerializer(read_only=True)
    region = RegionSerializer(read_only=True)
    likes = LikeSerializer(many=True)
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['likes'] = instance.likes.filter(like=True).count()
    #     return representation
    class Meta:
        model = Car
        fields = '__all__'




