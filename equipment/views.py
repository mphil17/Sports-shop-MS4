from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Equipment, Category

# Create your views here.


def show_equipment(request):

    equipment = Equipment.objects.all()
    query = None
    categories = None
    global sort
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            equipment = equipment.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            equipment = equipment.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please enter a search")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)| Q(condition__icontains=query)
            equipment = equipment.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'equipment': equipment,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'equipment/equipment.html', context)


def equipment_item(request, item_id):

    item = get_object_or_404(Equipment, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'equipment/equipment_item.html', context)


def sell(request):
    return render(request, 'equipment/sell.html')


def sell_form(request):

    if request.method == 'POST':
        sell_data = {
            'category': request.POST['category'],
            'name': request.POST['name'],
            'description': request.POST['description'],
            'condition': request.POST['condition'],
            'price': request.POST['price'],
        }
        sell_form = Equipment(category=category, name=name, description=description, condition=condition, price=price)
        sell_form.save()
    return render(request, 'equipment/sell.html')
