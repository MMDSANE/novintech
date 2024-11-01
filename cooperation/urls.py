from django.urls import path
from . import views

app_name = "cooperation"
urlpatterns = [
    path('', views.cooperation, name='cooperation'),
]
