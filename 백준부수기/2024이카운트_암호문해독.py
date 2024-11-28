def find(x):
	visited = set()
	
	while x in parents and parents[x] != x:
		if x in visited:
			return '?'
		visited.add(x)
		x = parents[x]
	
	return x

input_string = input()
n = int(input())
parents = {}

for _ in range(n):
	a, b = input().split()
	parents[a] = b
	
for c in input_string:
	print(find(c), end='')
	

	