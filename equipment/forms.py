from django import forms
from .models import Equipment, Category


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = ('category', 'name',
                  'description', 'condition',
                  'price', 'image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class AdminForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names