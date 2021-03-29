from django.contrib import admin
from .models import Equipment, Category

# Register your models here.


class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'condition',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Category, CategoryAdmin)
