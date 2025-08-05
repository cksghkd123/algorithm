def data_check(data):
    queue = []
    for i, v in enumerate(data):
        x, r = v
        queue.append((x-r, 0, i))
        queue.append((x+r, 1, i))

    queue.sort()

    stack = []

    for _, flag, idx in queue:
        if flag == 0:
            stack.append(idx)
        else:
            if stack[-1] != idx:
                return 'NO'
            stack.pop()

    return 'YES'


N = int(input())
circle_data = [list(map(int, input().split())) for _ in range(N)]

answer = data_check(circle_data)

print(answer)


