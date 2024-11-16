from django.urls import path
from . import views

app_name = "portfolio2"
urlpatterns = [
    path('portfolio2/', views.portfolio2, name='portfolio2'),
]
