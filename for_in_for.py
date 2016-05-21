# arr = [
# 	[1,1,1],
# 	[1,1,1],
# 	[1,1,1]
# ]

arr = [
	['a','a','a'],
	['a','a','a'],
	['a','a','a']
]


#dont work
for line in arr:
	for elm in line:
		elm = 2

print arr

#works
for line in range(len(arr)):
	for elm in range(len(arr[line])):
		arr[line][elm] = 'b'

print arr