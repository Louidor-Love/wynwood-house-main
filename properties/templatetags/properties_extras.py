"""Properties Tag Extras"""

# define un filtro de plantilla personalizado para Django 
from django import template #permite registrar filtros y etiquetas personalizados para su uso en las plantillas 

register = template.Library() #crea una instancia de Library, que se usa para registrar los filtros y etiquetas 


@register.filter(name='get_photos') #permite que el filtro sea utilizado en las plantillas de Django con este nombre.
def get_photos(property):
    return property.get_photos()
