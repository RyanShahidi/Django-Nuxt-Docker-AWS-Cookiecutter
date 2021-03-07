from django.urls import path
from apps.core.api import views as cv

urlpatterns = [
    path("healthcheck/", cv.HealthCheckView, name="eb-healthcheck"),
]
