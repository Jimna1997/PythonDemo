from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from travelo2 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('travelo2app.urls')),
    path('accounts/',include('accounts.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)