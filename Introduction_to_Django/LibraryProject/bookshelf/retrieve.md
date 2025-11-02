```python

from bookshelf.models import Book



\# Retrieve all Book instances

books = Book.objects.all()

for b in books:

&nbsp;   print(b.title, b.author, b.publication\_year)



\# Output:

\# 1984 George Orwell 1949

