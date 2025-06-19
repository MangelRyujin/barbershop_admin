from django.urls import path,include
from apps.haircuts.views.gallery_views import *

urlpatterns = [
    path('',gallery,name='gallery'),
    path('filter',gallery_table_results,name='gallery_table_results'),
    path('create',gallery_create,name='gallery_create'),
    path('delete/<int:pk>/',gallery_delete,name='gallery_delete'),
    
    
]

