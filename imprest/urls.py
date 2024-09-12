from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('logout',views.logout_user),
    path('ledger/', include('ledger.urls')),
]
