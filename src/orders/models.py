from django.db import models

from carts.models import Cart

ORDER_STATUS_CHOICES = (
		('created','Created'),
		('paid','Paid'),
		('shipped','Shipped'),
		('refunded','Refunded')
	)

class Order(models.Model):
	"""docstring for Order"""
	order_id = models.CharField(max_length=120, blank=True)
	# billing_profile
	# shipping_address
	# billing_address
	cart 			= models.ForeignKey(Cart)
	status 			= models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
	shipping_total 	= models.DecimalField(default=5.99, max_digits=50,  decimal_places=2)
	total     		= models.DecimalField(default=0.00, max_digits=50,  decimal_places=2)
		
	def __str__(self):
		return self.order_id

	# generate the order_id - probably using signals.
	# generate the order_total - probably using signals.