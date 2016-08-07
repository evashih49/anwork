from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20)
    keyman = models.CharField(max_length=20,  blank=True)
    contact_information = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15,  blank=True)
    address = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name

class Customer_Product(models.Model):
    customer = models.ForeignKey(Customer)
    product_name = models.CharField(max_length=100)
    spec = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return  self.product_name
	
class Order(models.Model):
    customer = models.ForeignKey(Customer)
    order_no = models.CharField(max_length=20)
    customer_orderno = models.CharField(max_length=20, blank=True)
    order_date = models.DateField()
    comment = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.order_no
	
class Order_Detail(models.Model):
    customer_product = models.ForeignKey(Customer_Product)
    order = models.ForeignKey(Order)
    order_qty = models.DecimalField(max_digits=6, decimal_places=0)
    ship_total_qty = models.DecimalField(max_digits=6, decimal_places=0)
    comment = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return str(self.customer_product) + ' ' +  str(self.order)
    class Meta:
        ordering = ['customer_product', 'order']
	
class Ship_Detail(models.Model):
    order_detail = models.ForeignKey(Order_Detail)
    ship_date = models.DateField()
    ship_qty = models.DecimalField(max_digits=6, decimal_places=0)
    blno = models.CharField(max_length=20,  blank=True)
    comment = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.order_detail)
	
    class Meta:
        ordering = ['order_detail']