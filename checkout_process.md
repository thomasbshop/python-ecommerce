# Checkout Process

1. Cart -> Checkout View
	- Login/Register or Enter an Email (as Guest)
	- Shipping Address
	- Billing info
		- Billing Address
		- Credit Card / Payment

2. Billing App / Component
	- Billing Profile
		- User or Email ( Guest Email)
		- Generate payment processor token. (Stripe or Braintree)

3. Orders / Invoices Component
	- Connecting the billing profile
	- Shipping / Billing Address
	- Cart
	- Status -- Shipped? Cancelled?