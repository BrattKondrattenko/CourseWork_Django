from django.urls import path

from event import views



urlpatterns = [
    path('', views.index, name='events'),
    path('tickets/', views.tickets, name='tickets'),
    
]
