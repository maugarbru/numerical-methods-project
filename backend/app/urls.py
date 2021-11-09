from django.urls import path
from .views import MethodListView

urlpatterns = [
    path('method/', MethodListView.as_view(), name='method_list')
]