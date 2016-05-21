def bar():
	return 100
def foo():
	def foo2():
		return 2 + bar()
	return foo2()

print foo()