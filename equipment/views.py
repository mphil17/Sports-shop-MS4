from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Equipment

# Create your views here.


def show_equipment(request):

    equipment = Equipment.objects.all()
    query = None

    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please enter a search")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)| Q(condition__icontains=query)
            equipment = equipment.filter(queries)

    context = {
        'equipment': equipment,
        'search_term': query,
    }

    return render(request, 'equipment/equipment.html', context)


def equipment_item(request, item_id):

    item = get_object_or_404(Equipment, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'equipment/equipment_item.html', context)
