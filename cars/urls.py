from django.contrib.sitemaps.views import index
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CarViewSet, CarCommentViewSet, LikeView

router = DefaultRouter()

router.register('information', CarViewSet)
router.register('comments', CarCommentViewSet)
router.register('likes', LikeView)

urlpatterns = [
    path('', index),
    path('', include(router.urls)),
]