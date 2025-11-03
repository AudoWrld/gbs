from django.shortcuts import render


def our_faculty(request):
    return render(request, "faculty/our_faculty.html")
