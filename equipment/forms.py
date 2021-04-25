from django import forms
from .models import Equipment


class SellForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('category', 'sku', 'name',
                  'description', 'condition',
                  'price', 'image',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'category': 'Sport Category',
            'name': 'Item',
            'description': 'Description',
            'condition': 'Condition',
            'price': 'Price',
        }

        self.fields['category'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
