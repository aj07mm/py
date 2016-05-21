# class Foo:
# 	a = 'a'
# 	__b = 'b'
# 	def __init__(self):

# 	def self.get_b():
# 		return __b

# foo1 = Foo()
# print foo1.get_b()

class Foo:
	x = 666

foo1 = Foo()

class Bar(Foo):
	i = 123 #class and instance variable
	self.instance_x = 111
	Bar.instance_x = 111

	@staticmethod #don't have self
	def static_get_x():
		return 9*9 + Bar.x
	#instance method
	def get_i(self): #unbound
		return 9*9 + self.i


	@staticmethod #don't have self
	def static_get_i():
		return 9*9 + Bar.i
	#instance method
	def get_i(self): #unbound
		return 9*9 + self.i

	def get_x(self): #superclass variable
		return self.x

	@classmethod #only receives Class and args as a Factory
	def foobar_classmethod(foo_cls, foo_args):
		return 9*9 + foo_cls.x#+ self.i


bar1 = Bar()

#THE SAME:
# print bar1.i
# print Bar.i

#THE SAME:
Bar.i = 999
print Bar.static_get_i()
print bar1.get_i()


print Bar.static_get_x()
print bar1.get_x()


# print Bar.foobar_classmethod(Foo)
# # a =  Bar().get_i()