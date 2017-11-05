class Product(object):
	def __init__(self, price, item_name, weight, brand):
		super(Product, self).__init__()
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = 'for sale'


	def sell(self):
		self.status = 'sold'
		print '%s sold!' % self.item_name
		return self


	def add_tax(self, tax):
		after_tax = self.price + self.price * tax
		print 'Price of %s after tax: %s' % (self.item_name, after_tax)
		return after_tax


	def return_product(self, condition):
		if condition == 'defective':
			self.price = 0
			self.status = 'defective'
		elif condition == 'used':
			self.price *= .8
			self.status = 'used'
		elif condition == 'new':
			self.status = 'for sale'
		print '%s returned in %s condition' % (self.item_name, condition)
		return self


	def display_info(self):
		print 'Price: $%s' % self.price
		print 'Item Name: %s' % self.item_name
		print 'Weight: %slbs' % self.weight
		print 'Brand: %s' % self.brand
		print 'Status: %s' % self.status
		return self


bird_food = Product(18, 'Hookbill Cuisine', 5, 'Perfect Parrot')

bird_food.sell().return_product('new').display_info()

