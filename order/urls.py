from django.urls import path

from order import views

urlpatterns = [
    path('', views.index, name='orders'),
    path('payments/', views.payment, name='payments'),

]
