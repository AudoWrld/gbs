from django.shortcuts import render


def our_programs(request):
    return render(request, "programs/our_programs.html")
