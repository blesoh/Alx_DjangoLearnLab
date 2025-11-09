import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

# Import your models
from .models import Author, Book, Library, Librarian


# -------------------------
# Example queries

def main():
    print("\n--- Query Examples ---\n")

    # 1. Query all books by a specific author
    try:
        author_name = "J.K. Rowling"  # Change to an actual author in your DB
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print("-", book.title)
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")

    # 2. List all books in a library
    try:
        library_name = "Central Library"  # Change to an actual library in your DB
        library = Library.objects.get(name=library_name)
        all_books = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in all_books:
            print("-", book.title)
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")

    # 3. Retrieve the librarian for a library
    try:
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian of {library_name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for library '{library_name}'")

if __name__ == "__main__":
    main() 
