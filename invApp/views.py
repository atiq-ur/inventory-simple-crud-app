from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Home View
def home_view(request):
    return render(request, 'home.html')

# Crate View
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'product_form.html', {"form": form})

#Read View
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {"products": products})


#Update View
def product_update_view(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'product_form.html', {"form": form})

# Delete View
def product_delete_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {"product": product})