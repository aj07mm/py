class Foo:
	bar = 1

class Foo2:
	def __init__(self):
		self.bar = 1 #instance variable

foo1 = Foo()
print foo1.bar

foo1 = Foo2()
print foo1.bar

print Foo.bar
print Foo2.bar


