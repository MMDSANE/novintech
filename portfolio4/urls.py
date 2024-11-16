from django.urls import path
from . import views

app_name = "portfolio4"
urlpatterns = [
    path('portfolio4/', views.portfolio4, name='portfolio4'),
]
