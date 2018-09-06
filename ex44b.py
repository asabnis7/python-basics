class Parent(object):
	
	def override(self):
		print "Parent Override"
		
class Child(Parent):
	
	def override(self):
		print "Child override"
		
dad = Parent()
son = Child()

dad.override()
# If derived class has declared function, calling function
# from derived object will call overriden function
son.override()