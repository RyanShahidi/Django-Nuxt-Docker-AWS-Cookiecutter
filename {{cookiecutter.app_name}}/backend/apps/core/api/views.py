from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from rest_framework import status

@api_view()
@permission_classes([AllowAny,])
def HealthCheckView(request):
    return Response(data=None, status=status.HTTP_200_OK)