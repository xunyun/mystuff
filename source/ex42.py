## Animal is-a object.
class Animal(object):
	pass
	
## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name
		
## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name
		
## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name
		## Person has-a pet of some kind
		self.pet = None
		
## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has-a name and salary. hmm what is this strange magic?
		super (Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	pass
	
##  Salman is-a Fish
class Salmon(Fish):
	pass
	
## Halibut is-a Fish
class Halibut(Fish):
	pass
	
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet 
mary.pet = satan

## frank is-a named "Frank" salary 12000 de Employee
frank = Employee("Frank", 120000)

## frank has-a a pet named rover 
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salman()

## ??
harry - Halibut()