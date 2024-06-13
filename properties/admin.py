"""Properties admin"""

# Django
from django.contrib import admin

# Models
from properties.models import Property, PropertyPhoto, City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

#muestra los formularios de los objetos relacionados en una disposición apilada 
class PropertyPhotoInline(admin.StackedInline): 
    model = PropertyPhoto
    extra = 3

#permite la edición de las fotos de una propiedad directamente en la página de detalles de esa propiedad
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin): 
    inlines = [PropertyPhotoInline,]
