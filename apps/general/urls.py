from django.urls import path,include
from apps.general.views.general_views import dashboard

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('haircuts/',include('apps.haircuts.urls.haircut_urls'))
]

