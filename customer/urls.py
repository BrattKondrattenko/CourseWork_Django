from django.urls import path

from customer import views

urlpatterns = [
    path('', views.customers, name='customers'),
    path('add/', views.add_customer, name='add')
]
