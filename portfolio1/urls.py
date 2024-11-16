from django.urls import path
from . import views

app_name = "portfolio1"
urlpatterns = [
    path('portfolio1/', views.portfolio1, name='portfolio1'),
]
