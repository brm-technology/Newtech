from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PictureViewSet

router = DefaultRouter()
router.register(r'pictures', PictureViewSet)

urlpatterns = [
    path('api/picture/', include(router.urls)),
]
