class Parent(object):

	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):

	def altered(self):
		print "CHILD, BEAFORE PARENT