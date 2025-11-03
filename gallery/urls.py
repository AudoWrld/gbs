from django.urls import path
from . import views

urlpatterns = [path("", views.our_gallery, name="gallery")]
