```python

from bookshelf.models import Book



\# Retrieve the book first (example: the first one)

book = Book.objects.first()



\# Delete the book

book.delete()



\# Check remaining books

Book.objects.all()



\# Output: <QuerySet \[]>

