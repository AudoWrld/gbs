from django.urls import path
from . import views

urlpatterns = [path("", views.our_faculty, name="our_faculty")]
