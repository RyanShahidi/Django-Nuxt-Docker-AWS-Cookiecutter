from django.urls import path, include
from apps.accounts.api.views import userAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', userAPIView)

urlpatterns = [
    path('accounts/', include(router.urls))
]
