from django.urls import path
from . import views

app_name = "landing_home"
urlpatterns = [
    path('', views.landing, name='landing_home'),  # مسیر اصلی سایت
    path('contact/', views.contact_view, name='contact'),  # مسیر فرم تماس
]
