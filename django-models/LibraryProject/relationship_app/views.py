from django.http import HttpResponse
from .models import Book

def list_books(request):
    """
    Return a simple text list of book titles and their authors.
    """
    books = Book.objects.select_related('author').all()
    lines = ["List of Books:"]
    for b in books:
        lines.append(f"{b.title} by {b.author.name}")
    text = "\n".join(lines)
    return HttpResponse(text, content_type="text/plain")
