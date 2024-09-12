from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_staff),
    path('staff_transactions/', views.staff_transactions),
    path('save_transaction/', views.save_transaction),
    path('all_transactions/', views.all_transactions),
    
]
