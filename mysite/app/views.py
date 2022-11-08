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

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_form = Contact(name=name, email=email, message=message)
        contact_form.save()
        messages.success(request, "You've successfully sent the message.")
        return redirect('contact')
    else:
        return render(request, 'contact.html')

def portfolio(request):
    if request.method == 'POST':
        context = {}
        category = request.POST.get('category')
        context['portfolios'] = Portfolio.objects.filter(category__slug=category)
        context['categories'] = Category.objects.all()
        return render(request, 'portfolio.html', context)
    else:
        context = {}
        context['categories'] = Category.objects.all()
        context['portfolios'] = Portfolio.objects.all()
        return render(request, 'portfolio.html', context)
        
def portfolioDetail(request, pk):
    context = {}
    context['portfolio'] = Portfolio.objects.get(id=pk)
    return render(request, 'portfolio-detail.html', context)