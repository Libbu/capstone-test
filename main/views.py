from django.shortcuts import render
from.models import About

def home_view(request):
    home = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "main/index.html")



