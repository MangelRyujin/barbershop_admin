from django.urls import path,include
from apps.haircuts.views.haircut_views import *

urlpatterns = [
    path('',haircut,name='haircut'),
    path('filter',haircut_table_results,name='haircut_table_results'),
    path('detail/<int:pk>/',haircut_detail,name='haircut_detail'),
    path('create',haircut_create,name='haircut_create'),
    path('update/<int:pk>/',haircut_update,name='haircut_update'),
    path('update-check/<int:pk>/',haircut_form_update,name='haircut_form_update'),
    path('delete/<int:pk>/',haircut_delete,name='haircut_delete'),

    
]

