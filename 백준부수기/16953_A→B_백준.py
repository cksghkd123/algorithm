import collections


A, B = map(int, input().split())

visited = set()

deq = collections.deque()

deq.append((A, 1))

answer = -1

while deq:
    number, count = deq.popleft()

    if number == B:
        answer = count
        break

    for next_number in [number*2, number*10+1]:
        if next_number <= B and next_number not in visited:
            visited.add(next_number)
            deq.append((next_number, count+1))


print(answer)

