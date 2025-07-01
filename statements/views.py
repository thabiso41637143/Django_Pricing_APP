from django.shortcuts import render
from .forms import ProductSelectForm
from .utils import consolidate_report, format_prod_data, products

def home(request):
    result = None
    selected_products = []
    if request.method == "POST":
        form = ProductSelectForm(request.POST)
        if form.is_valid():
            selected_products = form.cleaned_data["products"]
            result = format_prod_data(consolidate_report(products, selected_products))
    else:
        form = ProductSelectForm()

    return render(request, "statements/home.html", {
        "form": form,
        "result": result,
        "selected": selected_products
    })
