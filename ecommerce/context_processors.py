
from .models import Category

def menu_categories(request): # NOMBRE DE LA FUNCION DEBEN SER IGUALES
    categories = Category.objects.all()
    print(categories)
    return {'menu_categories': categories} # NOMBRE DEL OBJETO LLAMABLE DEBEN SER IGUALES