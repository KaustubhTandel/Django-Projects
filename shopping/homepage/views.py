from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def index(request):
    featured_products = Product.objects.filter(is_featured=True)[:6]
    all_products = Product.objects.all()
    categories = Category.objects.all()
    
    # Filter by category if requested
    category_id = request.GET.get('category')
    if category_id:
        all_products = all_products.filter(category_id=category_id)
    
    context = {
        'featured_products': featured_products,
        'all_products': all_products,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
    }
    return render(request, 'index.html', context)

def product_detail(request):
    product = get_object_or_404(Product)
    related_products = Product.objects.filter(
        category=product.category
    )
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'product_detail.html', context)
