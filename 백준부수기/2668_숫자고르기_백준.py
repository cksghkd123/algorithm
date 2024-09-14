def circles(start, n, result):
    if not visited[n]:
        visited[n] = True
        return circles(start, numbers[n], result + [n])
    
    if visited[n] and n == start:
        return result
    
    return []

N = int(input())

numbers = [int(input())-1 for _ in range(N)]

answer = set()

for i in range(N):
    visited = [False for _ in range(N)]
    answer.update(circles(i, i, []))

answer = list(answer)
answer.sort()

print(len(answer))

for a in answer:
    print(a+1)