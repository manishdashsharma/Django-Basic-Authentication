from django.urls import path
from .views import *

urlpatterns = [
    # job portal-------------------------------------------
    path("", serverStatus.as_view()),
    path("auth/", auth.as_view()),
    path("test/", SecureEndPoint.as_view()),
]