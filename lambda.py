


arr = ['a', 'b', 'c', 'd']
arrNums = range(1,5)
print arrNums

def foo_reduce(memo, current):
	memo.append(current + 'bar')
	return memo

def sum_reduce(memo, current):
	memo = memo * current
	return memo

def foo_map(memo, current):
	return 1


# print reduce(foo_reduce, arr, [])
print reduce(sum_reduce, arrNums, 1)

# print map(foo_map, arr, [])