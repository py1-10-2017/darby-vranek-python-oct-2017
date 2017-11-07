class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health


	def walk(self):
		print '%s is walking' % self.name
		self.health -= 1
		return self


	def run(self):
		print '%s is running' % self.name
		self.health -= 5
		return self


	def display_health(self):
		print '%s\'s health: %s' % (self.name, self.health)
		return self


class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, name):
		super(Dog, self).__init__(name, 150)


	def pet(self):
		print '%s has been pet' % self.name
		self.health += 5
		return self


class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name, 170)


	def fly(self):
		print '%s is flying' % self.name
		self.health -= 10
		return self


	def display_health(self):
		super(Dragon, self).display_health()
		print 'I am a dragon'
		return self


ginger = Animal('Ginger', 100)
ginger.walk().walk().walk().run().run().display_health()


boomer = Dog('Boomer')
boomer.walk().walk().walk().run().run().pet().display_health()


addie = Dragon('Addie')
addie.fly().fly().fly().display_health()


lydia = Animal('Lydia', 50)
lydia.display_health()