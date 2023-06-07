from django import forms

# from products.models import COLOR_CHOICES


class CreateItemForm(forms.Form):
    title = forms.CharField(max_length=255)
    price = forms.FloatField(min_value=0, max_value=10000, step_size=0.01)
    description = forms.CharField(max_length=1023)

