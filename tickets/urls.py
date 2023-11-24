"""
URL configuration for tickets project.

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from tickets import settings
from event.viewsets import TicketViewSet, EventViewSet
from customer.viewsets import CustomerViewSet
router = routers.DefaultRouter()
router.register(r'tickets', TicketViewSet)
router.register(r'events', EventViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
                  path('api/', include(router.urls)),
                  path('admin/', admin.site.urls),
                  path('orders/', include("order.urls")),
                  path('', include("customer.urls")),
                  path('events/', include("event.urls")),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
