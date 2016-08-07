from django.shortcuts import render_to_response

from csorder.models import Order
from django.db import connection


def home(request):
        return render_to_response('home.html')
		
def listdata(request):
    cursor = connection.cursor()
    cursor.execute("update csorder_order_detail set ship_total_qty = 0;")
	
    sqltx = ("UPDATE csorder_order_detail SET ship_total_qty = "
        " (SELECT sum(ship_qty) FROM csorder_ship_detail WHERE order_detail_id  = csorder_order_detail.id "
        " group by csorder_ship_detail.order_detail_id ) WHERE csorder_order_detail.id "
        " IN (SELECT order_detail_id  FROM csorder_ship_detail WHERE order_detail_id= csorder_order_detail.id);")
    cursor.execute(sqltx)
	
    sqltx = ("select csorder_customer.name,csorder_customer_product.product_name,csorder_order.customer_orderno,"
        " csorder_order.order_date,csorder_order_detail.order_qty, csorder_ship_detail.ship_date, csorder_ship_detail.ship_qty,"
        " csorder_order_detail.ship_total_qty,csorder_order_detail.order_qty - csorder_order_detail.ship_total_qty" 
        " from csorder_order_detail"
        " left outer join csorder_ship_detail  on csorder_ship_detail.order_detail_id = csorder_order_detail.id"
        " inner join csorder_order on csorder_order_detail.order_id = csorder_order.id "
        " inner join csorder_customer_product on csorder_order_detail.customer_product_id = csorder_customer_product.id"
        " inner join csorder_customer on csorder_order.customer_id = csorder_customer.id "
        " where csorder_order_detail.order_qty > csorder_order_detail.ship_total_qty; ")
    alldata = cursor.execute(sqltx)
	
    return  render_to_response('listdata.html', locals())