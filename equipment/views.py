from django.shortcuts import render
from .models import Equipment

# Create your views here.


def show_equipment(request):

    equipment = Equipment.objects.all()

    context = {
        'equipment': equipment,
    }

    return render(request, 'equipment/equipment.html', context)
