from django.shortcuts import render


def courses(request):
    return render(request, "applications/courses.html")
