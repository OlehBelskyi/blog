from django.urls import path
from .views import *

urlpatterns = [
    path('', CreateUserAPIView.as_view())
]
