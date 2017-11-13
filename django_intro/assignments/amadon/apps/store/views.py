from django.shortcuts import redirect, render
products = {
	'0': { 'name': 'Dojo T-Shirt', 'price': 19.99 },
	'1': { 'name': 'Dojo Sweater', 'price': 29.99 },
	'2': { 'name': 'Dojo Cup', 'price': 4.99 },
	'3': { 'name': 'Algorithm Book', 'price': 49.99}
}

def index(request):
	return render(request, 'store/index.html', context={'products': products})


def buy(request, product_id):
	if not 'purchase_count' in request.session:
		request.session['purchase_count'] = 0
	if not 'total_spent' in request.session:
		request.session['total_spent'] = 0
	quantity = int(request.POST['quantity'])
	product = products[product_id]
	total = quantity * product['price']
	request.session['recent_price'] = total
	request.session['purchase_count'] += quantity
	request.session['total_spent'] += total
	# print type(request.session['total_spent'])
	return redirect('/checkout')



def checkout(request):
	return render(request, 'store/checkout.html')
