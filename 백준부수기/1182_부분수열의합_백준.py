import sys 
from itertools import combinations 


n, s = map(int, sys.stdin.readline().split()) 
arr = list(map(int, sys.stdin.readline().split())) 
cnt = 0 

for r in range(1, n+1): 
    cm = combinations(arr, r) 
    for c in cm: 
        if sum(c) == s: 
            cnt += 1 
    
print(cnt)
