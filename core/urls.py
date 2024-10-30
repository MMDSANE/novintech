from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("landing.urls")),
    path("about_us/", include("about_us.urls")),
    path("about_me/", include("about_me.urls")),

]
