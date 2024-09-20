from apps.models import Todo, Book, Car
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from apps.models import Product


def todo_list_view(request):
    context = {
        "todos": Todo.objects.all(),
    }
    return render(request, 'apps/todo-list.html', context=context)


def todo_delete_view(request, pk):
    Todo.objects.filter(pk=pk).delete()
    return redirect('todo-list')


def todo_update_view(request, pk):
    if request.method == "POST":
        title = request.POST.get('name')
        Todo.objects.filter(pk=pk).update(name=title)
    return redirect('todo-list')


def todo_add_view(request):
    if request.method == "GET":
        name = request.GET.get('name')
        if name:
            Todo.objects.create(name=name)
    return redirect('todo-list')


# ---------------------------------------------------------------------------------------
"""Product Form"""


def product_add_view(request):
    if request.method == 'POST':
        d = {
            "name": request.POST.get('name'),
            "image": request.POST.get('image'),
            "price": request.POST.get('price'),
            "discount": request.POST.get('discount'),
        }
        Product.objects.create(**d)
        return redirect('product-form')
    return render(request, 'apps/product-form.html')


def product_form_view(request):
    products = Product.objects.all()
    return render(request, 'apps/product-form.html', {'products': products})


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.image = request.POST.get('image')
        product.price = request.POST.get('price')
        product.discount = request.POST.get('discount')
        product.save()
        return redirect('product-form')
    return redirect('product-form')


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product-form')


# ---------------------------------------------------------------------------------------
"""Book Form"""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


def book_add_view(request):
    if request.method == 'POST':
        d = {
            "name": request.POST.get('name'),
            "author": request.POST.get('author'),
            "image": request.POST.get('image'),
            "price": request.POST.get('price'),
        }
        Book.objects.create(**d)
        return redirect('book-form')  # Redirect after adding

    return render(request, 'apps/book-form.html')


def book_form_view(request):
    books = Book.objects.all()  # Get all books for display
    return render(request, 'apps/book-form.html', {'books': books})


def book_update_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.name = request.POST.get('name')
        book.author = request.POST.get('author')
        book.image = request.POST.get('image')
        book.price = request.POST.get('price')
        book.save()
        return redirect('book-form')  # Redirect after updating

    return render(request, 'apps/book-form.html', {'book': book})  # Pass book for pre-filling


def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book-form')  # Redirect after deletion


# --------------------------------------------------------------------------------------------------
"""Car Form"""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Car


def car_add_view(request):
    if request.method == 'POST':
        d = {
            "make": request.POST.get('make'),
            "model": request.POST.get('model'),
            "year": request.POST.get('year'),
            "color": request.POST.get('color'),
            "vin": request.POST.get('vin'),
            "transmission_type": request.POST.get('transmission'),
            "mileage": request.POST.get('mileage'),
            "fuel_type": request.POST.get('fuel'),
            "condition": request.POST.get('condition'),
        }
        Car.objects.create(**d)
        return redirect('car-form')

    return render(request, 'apps/car-form.html')


def car_form_view(request):
    cars = Car.objects.all()
    return render(request, 'apps/car-form.html', {'cars': cars})


def car_update_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.make = request.POST.get('make')
        car.model = request.POST.get('model')
        car.year = request.POST.get('year')
        car.color = request.POST.get('color')
        car.vin = request.POST.get('vin')
        car.transmission_type = request.POST.get('transmission')
        car.mileage = request.POST.get('mileage')
        car.fuel_type = request.POST.get('fuel')
        car.condition = request.POST.get('condition')
        car.save()
        return redirect('car-form')

    return render(request, 'apps/car-form.html', {'car': car})


def car_delete_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    return redirect('car-form')
