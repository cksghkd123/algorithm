import collections


def case(N):
    plus1 = N+1
    minus1 = N-1
    double = 2*N
    
    return plus1,minus1,double

def HNS(N,K):
    if N >= K:
        count = N - K
        return count
    
    visited = [0 for _ in range(100000*2 + 1)]
    deq = collections.deque()
    onetime = collections.deque()
    deq.append(N)
    count = 0
    visited[N] = 1

    while deq:
        count += 1

        while deq:
            onetime.append(deq.popleft())

        while onetime:
            N = onetime.popleft()
            n1, n2, n3 = case(N)
            n = [n1,n2,n3]

            if n1 == K or n2 == K or n3 == K:
                return count
            
            for w in n:
                if 0 <= w <= 100000:
                    if visited[w] == 0:
                        deq.append(w)
                        visited[w] = 1



N, K = map(int,input().split())

print(HNS(N,K))