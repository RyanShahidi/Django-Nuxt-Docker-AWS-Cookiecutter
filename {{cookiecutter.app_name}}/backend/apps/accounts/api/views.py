from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions, viewsets, mixins, status
from apps.accounts.api.serializers import UserDisplaySerializer, PasswordResetSerializer
from django.contrib.auth.tokens import default_token_generator
from apps.accounts.api.permissions import IsUserOrReadOnly
from apps.accounts.models import CustomUser

class userAPIView(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = UserDisplaySerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = CustomUser.objects.all()
    token_generator = default_token_generator

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()