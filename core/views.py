from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import get_user_model
from .serializers import AdminPasswordChangeSerializer, UserSerializer, UserDeleteSerializer
from .permissions import IsSuperUser


User = get_user_model()

class AdminPasswordChangeView(APIView):
    permission_classes = [IsSuperUser] 

    def get(self, request):
        """
        Returns a list of all users (only for superusers).
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Updates the password of the specified user (only for superusers).
        """
        serializer = AdminPasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update_password()
            return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDeleteView(APIView):
    permission_classes = [IsSuperUser]  # Only superusers can delete users

    def get(self, request):
        """
        Returns a list of all usernames (only for superusers).
        """
        users = User.objects.all()
        usernames = [user.username for user in users]
        return Response(usernames, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Deletes a user (only for superusers).
        """
        serializer = UserDeleteSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            try:
                user = User.objects.get(username=username)
                user.delete()
                return Response({"message": f"User '{username}' has been deleted."}, status=status.HTTP_204_NO_CONTENT)
            except User.DoesNotExist:
                return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


