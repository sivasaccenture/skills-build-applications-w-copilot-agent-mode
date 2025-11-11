"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.http import JsonResponse
import os

codespace_name = os.environ.get('CODESPACE_NAME', '')
codespace_url = f"https://{codespace_name}-8000.app.github.dev" if codespace_name else "http://localhost:8000"

def api_root(request):
    return JsonResponse({
        "users": f"{codespace_url}/api/users/",
        "teams": f"{codespace_url}/api/teams/",
        "activities": f"{codespace_url}/api/activities/",
        "workouts": f"{codespace_url}/api/workouts/",
        "leaderboard": f"{codespace_url}/api/leaderboard/",
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('', api_root, name='api-root'),
        # Add actual endpoints here, e.g.:
        # path('users/', ...),
        # path('teams/', ...),
        # path('activities/', ...),
        # path('workouts/', ...),
        # path('leaderboard/', ...),
    ])),
    path('', api_root),
]
