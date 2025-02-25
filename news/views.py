from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer

# Custom permission to allow only superusers to post, update, and delete
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser  # Allow only superusers

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [IsAuthenticated()]  # Allow all authenticated users to read
        elif self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsSuperUser()]  # Only allow superusers to modify content
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"detail": "Only admin users can create news."}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"detail": "Only admin users can update news."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"detail": "Only admin users can delete news."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
