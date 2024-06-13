from django.shortcuts import render #Facilita la creación de respuestas HTTP con datos renderizados en plantillas HTML
from typing import Any # indica que una variable o un valor puede ser de cualquier tipo.
from django.views.generic import ListView #una vista genérica de Django que muestra una lista de objetos

from .models import*

#vistas basadas en clases usando vista generica de Django.
class LandingPageView(ListView):
    model = Property
    template_name = 'landing.html'
    context_object_name = 'properties'
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        city_id = self.request.GET.get('city')
        if city_id:
            context['cities'] = City.objects.filter(id=city_id)
        else:
            context['cities'] = City.objects.all()

        context['Properties'] = Property.objects.all()
        context['guest_count'] = self.request.GET.get('guest_count', '')

        return context


    def get_queryset(self):
        queryset = super().get_queryset()
        arrival_date = self.request.GET.get('arrival_date')
        departure_date = self.request.GET.get('departure_date')
        guest_count = self.request.GET.get('guest_count')
        city_id = self.request.GET.get('city')
        
        if arrival_date:
            queryset = queryset.filter(arrival_date=arrival_date)
        if departure_date:
            queryset = queryset.filter(departure_date =departure_date) 
        if guest_count:
            queryset = queryset.filter(guest_count=guest_count)
        if city_id:
            queryset = queryset.filter(city_id=city_id)    
        
        return queryset  
