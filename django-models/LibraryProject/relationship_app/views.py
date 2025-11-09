# LibraryProject/relationship_app/views.py

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from .models import Book, Library

# -------------------------
# Function-based view (plain text)
# -------------------------
def list_books(request):
    """
    Return a simple text/plain list of book titles and their authors.
    Example output:
        List of Books:
        Harry Potter 1 by J.K. Rowling
        Some Book by Some Author
    """
    books = Book.objects.select_related('author').all()
    lines = ["List of Books:"]
    for b in books:
        lines.append(f"{b.title} by {b.author.name}")
    text = "\n".join(lines)
    return HttpResponse(text, content_type="text/plain")


# -------------------------
# Class-based view (HTML)
# -------------------------
class LibraryDetailView(DetailView):
    """
    Shows details for a single Library and lists its books.
    Uses template at: relationship_app/library_detail.html
    """
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    #
