from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # import redirect view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('LibraryProject.relationship_app.urls')),  # include app URLs
    path('', RedirectView.as_view(url='/relationship/')),  # redirect root / to /relationship/
]
