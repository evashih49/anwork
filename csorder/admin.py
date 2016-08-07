from django.contrib import admin

from csorder.models import Customer, Customer_Product, Order, Order_Detail,  Ship_Detail


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name',  'keyman', 'contact_information' , 'phone_number', 'address')
    search_fields = ('name',)
    ordering = ('name', )


class Customer_ProductAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product_name', 'spec', 'comment')
    ordering = ('customer',)
    def customer_name(self, instance):
        return instance.customer.name
	
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'order_no', 'customer_orderno', 'order_date', 'comment')
    ordering = ('-order_date', 'customer',)
    def customer_name(self, instance):
        return instance.customer.name

class Order_DetailAdmin(admin.ModelAdmin):
    list_display = ('customer_product', 'order', 'order_qty', 'comment')
    fileds = ('customer_product', 'order', 'order_qty', 'comment')
    ordering = ('customer_product' ,'order' ,)
		
class Ship_DetailAdmin(admin.ModelAdmin):
    list_display = ('order_detail', 'ship_date', 'ship_qty', 'blno', 'comment')
	

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Customer_Product, Customer_ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_Detail, Order_DetailAdmin)
admin.site.register(Ship_Detail, Ship_DetailAdmin)