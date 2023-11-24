from django.db.models import Q
from rest_framework import viewsets, filters

from customer.models import Customer
from customer.pagination import CustomerPagination
from customer.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['gender']
    search_fields = ['first_name', 'last_name', 'email']
    pagination_class = CustomerPagination

    def filter_customers(self):
        queryset = Customer.objects.all()

        first = self.request.query_params.get('first_name')
        last = self.request.query_params.get('last_name')
        email = self.request.query_params.get('email')

        queryset = queryset.filter(Q(first_name__startswith=first) | Q(last_name__startswith=last) | Q(email__startswith=email))
        return queryset
