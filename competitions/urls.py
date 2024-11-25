from django.urls import path
from . import views

app_name = "competitions"
urlpatterns = [
    path('', views.competitions, name='competitions'),
]
