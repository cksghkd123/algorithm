import collections


def bfs(subin, sister):
    deq = collections.deque()
    visited[subin] == True
    deq.append(subin)
    while deq:
        spot= deq.popleft()
        if spot > sister:
            if 0 <= spot-1 and visited[spot-1] == False:
                visited[spot-1] = True
                trace[spot-1] = spot
                deq.append(spot-1)
        elif spot == sister:
            result = [sister]
            while spot != subin:
                spot = trace[spot]
                result.append(spot)
            result.reverse()
            print(len(result)-1)
            return result
        else:
            for next_spot in (spot+1, spot-1, spot*2):
                if 0 <= next_spot < 100001 and visited[next_spot] == False:
                    visited[next_spot] = True
                    trace[next_spot] = spot
                    deq.append(next_spot)


n, k = map(int,input().split())
visited = [False] * 100001
trace = [0]*100001
result = bfs(n, k)
print(*result)