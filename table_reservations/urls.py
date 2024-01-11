from django.urls import path
from .views import my_page

urlpatterns = [
    path('my_page/', my_page, name='my_page'),
]
