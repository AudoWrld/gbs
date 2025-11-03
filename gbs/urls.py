from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("gbs-blog/", include("blogs.urls")),
    path("gbs-faculty/", include("faculty.urls")),
    path("gbs-gallery/", include("gallery.urls")),
    path("gbs-programs/", include("programs.urls")),
    path("donation/", include("donation.urls")),
]
