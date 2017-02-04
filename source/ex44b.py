class Parent(object):

	def override(self):
		print "PARENT oberride()"
		
class Child(Parent):

	def override(self):
		print "CHILD override()"
		
dad = Parent()
son = Child()

dad.override()
son.override()
		