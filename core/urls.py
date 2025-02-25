from django.urls import path, include
from .views import AdminPasswordChangeView, UserDeleteView

urlpatterns = [
    path('password/change-password/', AdminPasswordChangeView.as_view(), name='admin-change-password'),
    path('delete/delete-user/', UserDeleteView.as_view(), name='admin-delete-user'),
]
