def solution(n, s, mod):
    return s * calculate(n, mod-2, mod) % mod 

def calculate(n, t, mod):
    if t == 1:
        return n % mod
    
    if t%2 == 0:
        half = calculate(n, t//2, mod) 
        return (half * half) % mod
    
    return n * calculate(n, t-1, mod) % mod

M = int(input())

answer = 0

for _ in range(M):
    N, S = map(int, input().split())

    answer += solution(N, S, 1000000007)
    answer %= 1000000007

print(answer)