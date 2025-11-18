

from django.urls import path
from market import views




urlpatterns = [
    path('get_product/',views.get_product),
    path('create_product/',views.create_product),
    path('update_product/<int:id>/',views.update_product),
    path('delete_product/<int:id>/',views.delete_product),
    
]