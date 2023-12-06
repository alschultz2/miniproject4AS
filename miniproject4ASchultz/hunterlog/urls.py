from django.urls import path
from .views import log_weapon

urlpatterns = [
    path('log_weapon/', log_weapon, name='log_weapon'),
    # Add more URLs as needed
]