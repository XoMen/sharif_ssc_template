from django.urls import path
from app_sharif import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.home),
    path('login/', views.login_),
    path('logout/', views.logout_),
    path('signup/', views.signup),
    path('profile/', views.profile),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
