class Parent(object):
	
	def override(self):
		print "PARENT override()111111"
		
	def implicit(self):
		print "PARENT implicit()111111"
		
	def altered(self):
		print "PARENT altered()111111"
		
class Child(Parent):

	def override(self):
		print "CHILD override()222222"
		
	def altered(self):
		print "CHILD, BEFORE PARENT altered()222222"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()222222"
		
		
dad = Parent()
son = Child()
print "-" * 30
dad.implicit()
son.implicit()
print "-" * 30
dad.override()
son.override()
print "-" * 30
dad.altered()
print "-  -  " * 10
son.altered()
print "-" * 30
dad.implicit()
dad.altered()
dad.override()
print "-" * 30
son.override()
son.implicit()
son.altered()