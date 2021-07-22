import collections


def case(N):
    plus1 = N+1
    minus1 = N-1
    double = 2*N
    
    return plus1,minus1,double

def HNS(N,K):
    deq = collections.deque()
    onetime = collections.deque()
    deq.append(N)
    count = 0

    while deq:
        count += 1

        while deq:
            onetime.append(deq.popleft())

        while onetime:
            N = onetime.popleft()
            n1, n2, n3 = case(N)
            if n1 == K or n2 == K or n3 == K:
                return count

            deq.extend([n1,n2,n3])


N, K = map(int,input().split())

print(HNS(N,K))