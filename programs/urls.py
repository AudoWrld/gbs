from django.urls import path
from . import views

urlpatterns = [path("", views.our_programs, name="our_programs")]
