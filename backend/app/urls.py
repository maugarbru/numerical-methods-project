from django.urls import path
from .views import IntegralsMethod, DerivatesMethod

urlpatterns = [
    path('integrales/', IntegralsMethod.as_view(), name='integrales_method'),
    path('derivadas/', DerivatesMethod.as_view(), name='derivadas_method')
]