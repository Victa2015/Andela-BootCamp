class Person (object):
	def __init__ (self, name):
		self.name = name
		
	def call(self):
		print ("Hello", format(self.name))

Collin = Person ("Collin")
Collin.call()