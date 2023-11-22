from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from core.forms import ContactForm
from django.urls import reverse
from core.models import *
# Create your views here.

def home(request):
    carousel_items = CarouselItem.objects.all()
    services = Service.objects.all()
    context={
        
        # "x":Service.objects.all(),
        # "x2":Service[0:8],
        'carousel_items': carousel_items,
        "title": "Ana Səhifə ",
        # 'mentor':Testimonial.objects.all(),
        'services' : services,    
    }
    return render(request, 'index.html', {'services': services,})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            form = ContactForm() 
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def about(request):
    context={
        'mentor':Testimonial.objects.all(),
        'about': About.objects.all()

    }
    return render(request, 'about.html', context)

def service (request):
    category = Category.objects.all()
    services = Service.objects.all()


    if "category" in request.GET.keys():        
        services = Service.objects.filter(
            category_id__title=request.GET["category"])
    
    # paginator = Paginator(products, 4)
    # page = request.GET.get('page')
    # products = paginator.get_page(page)
   
    context = {
        'page_obj': Service,
        'mehsul': Service,
        'category': Service,
       
    }
    return render(request, 'service.html', context)

def warning(request):
    context={
        'mentor':Testimonial.objects.all(),
        'warnings': Warnings.objects.all()

    }
    return render(request, '404.html', context)

def team (request):
    categories = Category.objects.all()
    team_ = Team.objects.all()

    if "category" in request.GET.keys():        
        team_ = Team.objects.filter(
            category_id__title=request.GET["category"])
    
    # paginator = Paginator(teams, 4)
    page = request.GET.get('page')
    # teams = paginator.get_page(page)
   
    context = {
        'page_obj': team_,
        'mehsul': team_,
        'category': categories,
       
    }
    return render(request, 'team.html', context)

def feature(request):
    context={
        'mentor':Testimonial.objects.all(),
        'features': Feature.objects.all()

    }
    return render(request, 'feature.html', context)

def appointment(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            form = ContactForm() 
    else:
        form = ContactForm()
    return render(request, 'appointment.html', {'form': form})