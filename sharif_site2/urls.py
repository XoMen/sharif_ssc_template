
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_sharif.urls')),
    url(r'^froala_editor/', include('froala_editor.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
