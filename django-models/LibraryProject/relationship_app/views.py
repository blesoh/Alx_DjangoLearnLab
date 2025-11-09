# LibraryProject/relationship_app/views.py

from django.shortcuts import render
from django.views import View
from .models import Book
from .models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    output = ""
    for book in books:
        output += f"{book.title} by {book.author.name}\n"
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show details of a specific library
class LibraryDetailView(View):
    def get(self, request, pk):
        library = Library.objects.get(pk=pk)
        return render(request, 'relationship_app/library_detail.html', {'library': library})
