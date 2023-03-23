from django.urls import path, include
from pay.views import order

urlpatterns = [
    path('', order),
]
