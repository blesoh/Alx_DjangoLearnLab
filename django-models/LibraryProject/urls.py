from django.contrib import admin
from django.urls import path, include
from LibraryProject.relationship_app import views  # Import your views

urlpatterns = [
    path('', views.list_books, name='home'),  # Root URL
    path('admin/', admin.site.urls),           # Admin URL
    path('relationship/', include('LibraryProject.relationship_app.urls')),  # Optional extra path
]
