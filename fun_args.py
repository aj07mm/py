def foo(*args, **kwargs):
	return kwargs

print foo(1, 2, 3, 4, [123], bar=1)