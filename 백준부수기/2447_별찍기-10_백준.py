init = ['***', '* *', '***']

N = int(input())

def recursion(n = 3, arr = init):

    if n == N:
        return arr

    tmp = []

    for i in range(n):
        tmp.append(arr[i] * 3)

    for i in range(n):
        tmp.append(arr[i] + ' ' * n + arr[i])

    for i in range(n):
        tmp.append(arr[i] * 3)

    return recursion(n * 3, tmp)

answer = recursion(3, init)

for line in answer:
    print(line)