
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_sharif.urls')),
    url(r'^froala_editor/', include('froala_editor.urls')),
]
