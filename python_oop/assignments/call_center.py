class Call(object):
	def __init__(self, id, name, number, time, reason):
		self.id = id
		self.name = name
		self.number = number
		self.time = time
		self.reason = reason


	def display(self):
		print 'ID: #%s' % self.id
		print 'Caller\'s name: %s' % self.name
		print 'Caller\'s number: %s' % self.number
		print 'Call Time: %s' % self.time
		print 'Reason for call: %s' % self.reason



class CallCenter(object):
	def __init__(self):
		self.calls = list()


	def add(self, call):
		self.calls.append(call)
		return self


	def remove(self):
		self.calls.pop(0)
		return self


	def info(self):
		print 'there are %s calls in the queue.' % len(self.calls)
		for call in self.calls:
			print '%s: %s' % (call.name, call.number)


	def remove_number(self, number):
		for call in self.calls:
			if call.number == number:
				self.calls.remove(call)