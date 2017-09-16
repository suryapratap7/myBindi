from django.shortcuts import render
from .models import Programs

def page_list(request):
    programs = Programs.objects.all()
    return render(request, 'blog/index.html', {'programs': programs})
