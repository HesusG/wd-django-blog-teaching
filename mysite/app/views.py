from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def blogs(request):
    context = {}
    context['articles'] = Blog.objects.all()
    return render(request, 'blogs.html', context)

def blogDetail(request, pk):
    context = {}
    context['article'] = Blog.objects.get(id=pk)
    return render(request, 'blog-detail.html', context)