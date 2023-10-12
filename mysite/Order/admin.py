
from django.contrib import admin

# Register your models here.
from Order.models import Orders, OrderUpdate


admin.site.register(Orders)
admin.site.register(OrderUpdate)
