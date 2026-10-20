from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('favicon.ico', serve, {'path': 'favicon.ico', 'document_root': settings.BASE_DIR / 'dashboard' / 'static'}),
    path('sikasep/favicon.ico', serve, {'path': 'favicon.ico', 'document_root': settings.BASE_DIR / 'dashboard' / 'static'}),
    path('admin/', admin.site.urls),
    path('sikasep/', include('dashboard.urls')),
    path('', include('dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/sikasep/media/', document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'dashboard' / 'static')
    urlpatterns += static('/static/', document_root=settings.BASE_DIR / 'dashboard' / 'static')
    urlpatterns += static('/sikasep/static/', document_root=settings.BASE_DIR / 'dashboard' / 'static')
    upload_root = getattr(settings, 'SIKASEP_UPLOAD_ROOT', settings.MEDIA_ROOT)
    urlpatterns += static('/uploads/', document_root=upload_root)
    urlpatterns += static('/sikasep/uploads/', document_root=upload_root)
