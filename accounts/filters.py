import django_filters
from django_filters import DateFilter
from .models import Order


class OrderFilter(django_filters.FilterSet):
	start_date= DateFilter(field_name="date_created",lookup_expr="gte")
	end_date= DateFilter(field_name="date_created",lookup_expr="lte")
	class Meta:
		model = Order
		fields = '__all__'
		exclude=['customer','date_created']
		include=['start_date','end_date']