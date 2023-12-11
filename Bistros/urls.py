from django.contrib import admin
from django.urls import path, include
from .views import index, menu
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('menu/', menu, name='menu'),
    path('auth/', include('Auth.urls')),
    path('client/', include('Clients.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)