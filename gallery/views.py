from django.shortcuts import render

def our_gallery(request):
    return render(request, "gallery/gallery.html")