from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("landing.urls")),
    path("about_us/", include("about_us.urls")),
    path("about_me/", include("about_me.urls")),
    path("blog/", include("blog.urls")),
    path("blog/", include("post.urls")),
    path("cooperation/", include("cooperation.urls")),
    path("contact_us/", include("contact_us.urls")),
    path("", include("portfolio1.urls")),
    path("", include("portfolio2.urls")),
    path("", include("portfolio3.urls")),
    path("", include("portfolio4.urls")),

]
