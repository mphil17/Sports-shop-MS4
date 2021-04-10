from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from equipment.models import Equipment


def bag_contents(request):

    bag_items = []
    total = 0
    delivery = 0
    product_count = 0
    bag = request.session.get('bag', {})


    print(bag)

    for bag_item, quantity in bag.items():
        equip_piece = get_object_or_404(Equipment, pk=bag_item)
        total += quantity * equip_piece.price
        product_count += quantity
        delivery = 2
        print(delivery)
        print(total)
        bag_items.append({
            'bag_item': bag_item,
            'equip_piece': equip_piece,
            'quantity': quantity,
        })

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
