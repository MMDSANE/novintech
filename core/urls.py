from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("landing.urls")),
    path("about_us/", include("about_us.urls")),
    path("about_me/", include("about_me.urls")),
    path("competitions/", include("competitions.urls")),
    path("competitions/", include("question.urls")),
    path("cooperation/", include("cooperation.urls")),
    path("contact_us/", include("contact_us.urls")),
    path("", include("portfolio1.urls")),
    path("", include("portfolio2.urls")),
    path("", include("portfolio3.urls")),
    path("", include("portfolio4.urls")),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)