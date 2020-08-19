from django.shortcuts import render
from django.views.generic import ListView
from books.models import Book

class BookListView(ListView):
    model = Book
    context_object_name = 'obj_list'
    template_name = 'books/book_list.html'
