from djoser.views import UserViewSet
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.views import View
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN,HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_204_NO_CONTENT
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .permissions import IsSuperAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from rest_framework.decorators import action

User = get_user_model()

class UserActivationView(UserViewSet):
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())

        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}

        return serializer_class(*args, **kwargs)

    def activation(self, request, uid, token, *args, **kwargs):
        try:
            response = super().activation(request, *args, **kwargs)
            if response.status_code == HTTP_204_NO_CONTENT:
                return render(request, 'user_activation.html', {'message': 'User activated successfully.'})
            else:
                return render(request, 'user_activation.html', {'message': 'Activation failed. Contact Admin.'})
        except PermissionDenied as e:
            return render(request, 'user_activation.html', {'message': 'Permission denied. Contact Admin.'})
        except Exception as e:
            return render(request, 'user_activation.html', {'message': 'Activation failed. Contact Admin.'})

class CustomPasswordResetConfirmView(View):
    def get(self, request, uidb64=None, token=None):
        user = self._get_user(uidb64)
        if user and default_token_generator.check_token(user, token):
            form = SetPasswordForm(user)
            return render(request, 'password_reset_form.html', {'form': form})
        else:
            return render(request, 'password_reset_message.html')

    def post(self, request, uidb64=None, token=None):
        user = self._get_user(uidb64)
        if user and default_token_generator.check_token(user, token):
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'password_reset_message.html', {'message': 'Password reset successfully.'})
            else:
                return render(request, 'password_reset_form.html', {'form': form})
        else:
            return render(request, 'password_reset_message.html')

    def _get_user(self, uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            print("hello",uid)
            return User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return None
        
# View to update user status
class UserStatusView(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserStatus
    permission_classes=[IsSuperAdmin]
    
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        if not request.user.role=='superadmin':
            return Response({'error':'Only superadmin can change the status'}, status=HTTP_403_FORBIDDEN)
        try:
            user = UserAccount.objects.get(pk=pk)
            if user.role == 'superadmin':
                print(user.role)
                return Response({'error': 'Superadmin cannot be deactivated.'}, status=HTTP_403_FORBIDDEN)
        except UserAccount.DoesNotExist:
            return Response({'error': 'User not found.'}, status=HTTP_403_FORBIDDEN)
        
        status = request.data.get('status')
        print(status)
        if status is not None:
            user.is_active = status
            user.save()
            return Response({'status': 'User status updated successfully.'}, status=HTTP_200_OK)
        return Response({'error': 'Status not provided.'}, status=HTTP_400_BAD_REQUEST)
    
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated,IsSuperAdmin]
    def get(self, request, *args, **kwargs):
        print(request.user.role)
        return Response({"message":f"this is protected view, logged in user is {request.user.role}"})