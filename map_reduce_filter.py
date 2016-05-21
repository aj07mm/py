def increment(x):
	return x + 1

# print map(increment, [1,2,3])


def sum(memo, current):
	return memo + current

# print reduce(sum, [1,2,3])


def odd(x):
	return x % 2 == 0

print filter(odd, [1,2,3])