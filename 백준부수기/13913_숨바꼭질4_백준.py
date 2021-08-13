import collections


def bfs(subin, sister):
    deq = collections.deque()
    deq.append((subin,[subin]))
    if subin > sister:
        return [i for i in range(subin,sister-1,-1)]

    while deq:
        spot, trace = deq.popleft()
        if spot > sister:
            deq.append((spot-1, trace + [spot-1]))
        elif spot == sister:
            return trace
        else:
            deq.append((spot+1, trace + [spot+1]))
            deq.append((spot-1, trace + [spot-1]))
            deq.append((spot*2, trace + [spot*2]))


n, k = map(int,input().split())
result = bfs(n, k)
print(result)