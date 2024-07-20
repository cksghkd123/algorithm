EMPTY = 'FRULA'

S = input()
c4_string = input()

c4_i = 0
c4_n = len(c4_string)

stack = []

for i in range(len(S)):
    stack.append(S[i])
    if len(stack) >= c4_n:
        for j in range(c4_n):
            if stack[-1-j] != c4_string[-1-j]: 
                break
        else:
            for _ in range(c4_n):
                stack.pop()

answer = ''.join(stack)

if answer == '':
    print(EMPTY)
else:
    print(answer)

# 12ab112ab2abcd
# 12ab


# 11123112112336
# 1123



