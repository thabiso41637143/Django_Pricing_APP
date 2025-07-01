from django import forms

class ProductSelectForm(forms.Form):
    PRODUCTS = [
        ("Credit Card", "Credit Card"),
        ("Overdraft", "Overdraft"),
        ("Guarantee", "Guarantee")
    ]
    products = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=PRODUCTS,
        required=True
    )
