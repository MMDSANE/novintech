from django.urls import path

from landing.urls import app_name
from . import views

app_name = "post"
urlpatterns = [
    path('post/', views.post, name='post'),
]
