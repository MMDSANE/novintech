from django.urls import path

from about_us.urls import app_name
from . import views

app_name = "landing_home"
urlpatterns = [
    path('', views.landing, name='landing_home'),
]
