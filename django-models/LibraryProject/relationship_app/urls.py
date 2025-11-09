from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register

from django.shortcuts import redirect

# Simple root redirect to login
def root_redirect(request):
    return redirect('login')

urlpatterns = [
    path('', root_redirect, name='root'),  # Redirect root URL to login
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
