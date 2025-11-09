from django.urls import path
from .views import list_books, register, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('', list_books, name='home'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
