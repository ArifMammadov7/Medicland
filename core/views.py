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