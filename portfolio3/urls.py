from django.urls import path
from . import views

app_name = "portfolio3"
urlpatterns = [
    path('portfolio3/', views.portfolio3, name='portfolio3'),
]
