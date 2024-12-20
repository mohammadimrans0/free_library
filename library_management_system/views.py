from django.shortcuts import render, get_object_or_404
from books.models import Book
from categories.models import Category

def main(request, category_slug=None):
    books = Book.objects.all()
    categories = Category.objects.all()
    # selected_category_ids = []
    selected_category_ids = None

    # Handle filtering by category
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)
        selected_category_ids.append(category.id)

    # If filtering by checkbox (via GET request)
    # if 'categories' in request.GET:
    #     selected_category_ids = request.GET.getlist('categories')
    #     books = books.filter(category__id__in=selected_category_ids)

    # If filtering by radio button (via GET request)
    if 'category' in request.GET:
        selected_category_id = request.GET.get('category')
        books = books.filter(category__id=selected_category_id)

    return render(
        request, 
        'index.html', 
        {'books': books, 'categories': categories, 'selected_category_ids': selected_category_ids}
    )
