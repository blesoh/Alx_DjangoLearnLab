from django.contrib import admin
from .models import Book

# Customize the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in admin list view
    search_fields = ('title', 'author')  # Add search capability
    list_filter = ('publication_year',)  # Add filter by year

# Register the Book model with the customized admin
admin.site.register(Book, BookAdmin)


# Register your models here.
