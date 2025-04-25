from django.urls import path
from .views import index, dashboard

urlpatterns = [
    path('', index, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
]