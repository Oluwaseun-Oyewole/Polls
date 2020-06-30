
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('votingapp.urls')),
    path('', include('pages.urls')),
]
