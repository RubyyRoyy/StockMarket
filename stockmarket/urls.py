from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('add_query', views.add_query, name='add_query'),
    # path('add_stock', views.add_stock, name='add_stock'),
    path('export_excel',views.export_excel, name = 'export_excel')
]