"""
URL configuration for spottdine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from main_site.views import main,Booking,Reting

from table_reservations.views import my_page

from main_site.views import main,Booking,Reting,galery_view,menu

from main_site.views import main,Booking,Reting,galery_view,menu,account_info
from main_site.views import search_restaurants

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/<int:booking_id>/', my_page, name='booking'),
    path('reting/<int:restoran_id>/', Reting, name="reting" ),
    path('galery/<int:zaved_id>/', galery_view, name='galery'),
    path('menu/<int:menu_id>/', menu, name='menu'),
    path('account/<int:zaved_id>/', account_info, name='account'),
    path('search/', search_restaurants, name='search_restaurants'),
    path('', main, name='main'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
