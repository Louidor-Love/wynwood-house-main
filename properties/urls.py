from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
] 