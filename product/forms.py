from django import forms
from .models import product

class productform(forms.ModelForm):
    class Meta:
        model=product
        fields=[
            'proid',
            'name',
            'file',
            'image1',
            'image2',
            'color',
            'size',
            'price',
        ]

        widgets={
            "size":forms.CheckboxSelectMultiple()
        }
        