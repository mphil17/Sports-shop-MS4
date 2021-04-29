from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Equipment, Category

from .forms import EquipmentForm, AdminForm

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
                return redirect(reverse('equipment'))

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


@login_required
def sell_equipment(request):
    """ Add a equipment to the store to sell """
    if not request.user:
        messages.error(request, 'Sorry, only sellers can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('sell_equipment'))
        else:
            messages.error(request, 'Failed to add item. Please ensure the form is valid.')
    else:
        form = EquipmentForm()
    template = 'equipment/sell.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def admin(request):
    """ Admin to control equipment """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('admin'))
        else:
            messages.error(request, 'Failed to add item. Please ensure the form is valid.')
    else:
        admin_form = AdminForm()
    template = 'equipment/admin.html'
    context = {
        'admin_form': admin_form,
    }

    return render(request, template, context)


@login_required
def admin_edit(request, item_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    equipment = get_object_or_404(Equipment, pk=item_id)
    if request.method == 'POST':
        form = AdminForm(request.POST, request.FILES, instance=equipment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated item!')
            return redirect(reverse('equipment_item', args=[equipment.id]))
        else:
            messages.error(request, 'Failed to update item. Please ensure the form is valid.')
    else:
        update_form = AdminForm(instance=equipment)
        messages.info(request, f'You are editing {equipment.name}')

    template = 'equipment/admin_edit.html'
    context = {
        'update_form': update_form,
        'equipment': equipment,
    }

    return render(request, template, context)


@login_required
def admin_delete(request, item_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    """ Delete a product from the store """
    equipment = get_object_or_404(Equipment, pk=item_id)
    equipment.delete()
    messages.success(request, 'Item deleted!')
    return redirect(reverse('equipment'))
