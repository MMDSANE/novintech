from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.landing, name='landing_home'),
]