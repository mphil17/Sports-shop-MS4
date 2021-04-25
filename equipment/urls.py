from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_equipment, name='equipment'),
    path('<int:item_id>/', views.equipment_item, name='equipment_item'),
    path('sell/', views.sell_equipment, name='sell_equipment'),
]
