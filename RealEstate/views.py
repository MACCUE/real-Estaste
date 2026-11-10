from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def starter_page(request):
    return render(request, 'starter-page.html')

def service_details(request):
    return render(request, 'service_details.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog_details.html')

def page(request):
    return render(request, 'page.html')
# Create your views here.
