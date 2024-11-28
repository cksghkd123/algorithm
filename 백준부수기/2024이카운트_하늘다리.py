N = int(input())
height_list = list(map(int, input().split()))

answer = 0
stack = []

i = 0
while i < N:
	h = height_list[i]
	if not stack:
		stack.append(h)
		i += 1
	else:
		if h < stack[-1]:
			stack.append(h)
			i += 1
		elif h > stack[-1]:
			stack.pop()
		else:
			i += 1
			answer += 1
	
print(answer)
			