from django.urls import path
from apps.views import product_add_view, product_form_view, product_update_view, product_delete_view, book_add_view, \
    book_form_view, book_update_view, book_delete_view, car_add_view, car_form_view, car_update_view, car_delete_view
from apps.views import todo_delete_view, todo_update_view, todo_list_view, todo_add_view

urlpatterns = [
    path('todo-list', todo_list_view, name='todo-list'),
    path('todo-delete/<int:pk>', todo_delete_view, name="todo-delete"),
    path('todo-update/<int:pk>', todo_update_view, name="todo-update"),
    path('todo-add', todo_add_view, name="todo-add"),

    path('product', product_add_view, name="product-add"),
    path('product-form', product_form_view, name="product-form"),
    path('product/update/<int:pk>/', product_update_view, name='product-update'),
    path('product/delete/<int:pk>/', product_delete_view, name='product-delete'),

    path('book', book_add_view, name="book-add"),
    path('book-form', book_form_view, name="book-form"),
    path('book/update/<int:pk>/', book_update_view, name='book-update'),
    path('book/delete/<int:pk>/', book_delete_view, name='book-delete'),

    path('car', car_add_view, name="car-add"),
    path('car-form', car_form_view, name="car-form"),
    path('car/update/<int:pk>/', car_update_view, name='car-update'),
    path('car/delete/<int:pk>/', car_delete_view, name='car-delete'),

]
