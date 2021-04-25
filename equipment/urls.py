from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_equipment, name='equipment'),
    path('<item_id>', views.equipment_item, name='equipment_item'),
    path('sell/', views.sell, name='sell'),
    path('sell_form/', views.sell_form, name='sell_form'),
]
