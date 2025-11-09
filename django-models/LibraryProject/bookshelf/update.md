```python

from bookshelf.models import Book



\# Retrieve the book first (example: the first one)

book = Book.objects.first()



\# Update the title

book.title = 'Nineteen Eighty-Four'

book.save()



\# Output: Book title updated successfully

