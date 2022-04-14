import collections

INF = float('inf')
def low_price():
    visited = [[INF for _ in range(3)] for _ in range(n)]
    answer = INF
    deq = collections.deque()
    deq.append([None, 0, 0])
    while deq:
        pre_collor, index, amount = deq.popleft()
        for i in range(3):
            if pre_collor == i:
                continue
            new_amount = amount + cost[index][i]
            if index+1 == n:
                answer = min(answer, new_amount)
            else:
                if new_amount < visited[index+1][i]:
                    visited[index+1][i] = new_amount
                    deq.append([i, index+1, new_amount])

    return answer

n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int,input().split())))

answer = low_price()
print(answer)
