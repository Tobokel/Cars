from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from cars.models import Car, CarComment, Like
from cars.permissions import IsAuthorOrIsAdmin
from cars.serializers import CarSerializer, CreateCarSerializer, CarDetailsSerializer, CarCommentSerializer, \
    LikeSerializer


class CarFilter(filters.FilterSet):


    class Meta:
        model = Car
        fields = ('id', 'name', 'sub_category', 'price')

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    # pagination_class = None
    serializer_class = CarSerializer
    filter_backends = [filters.DjangoFilterBackend, rest_filters.SearchFilter, rest_filters.OrderingFilter]
    filterset_class = CarFilter
    search_fields = ['name', 'sub_category', 'price']
    ordering_fields = ['id', 'name', 'created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return CarSerializer
        elif self.action == 'retrieve':
            return CarDetailsSerializer
        return CreateCarSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return []

class CarCommentViewSet(viewsets.ModelViewSet):
    queryset = CarComment.objects.all()
    serializer_class = CarCommentSerializer

    class Meta:
        model = CarComment
        fields = '__all_'

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAuthorOrIsAdmin()]
        return []

    @action(['GET'], detail=True)
    def comments(self, request, pk=None):
        car = self.get_object()
        comments = car.comments.all()
        serializer = CarCommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)


class LikeView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    lookup_field = 'car'

    class Meta:
        model = Like
        fields = '__all__'