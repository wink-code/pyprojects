"""URL patterns for the users app.

This file was missing at the project root. It delegates to Django's
authentication URL patterns.
"""

from django.urls import include, path
from . import views

app_name = 'users'

urlpatterns = [
    # include the default auth views (login, logout, password reset, etc.)
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
