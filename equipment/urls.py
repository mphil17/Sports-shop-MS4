from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_equipment, name='equipment'),
    path('<int:item_id>/', views.equipment_item, name='equipment_item'),
    path('sell/', views.sell_equipment, name='sell_equipment'),
    path('admin/', views.admin, name='admin'),
    path('admin_edit/<int:item_id>/',
         views.admin_edit, name='admin_edit'),
    path('admin_delete/<int:item_id>/',
         views.admin_delete, name='admin_delete'),
]
