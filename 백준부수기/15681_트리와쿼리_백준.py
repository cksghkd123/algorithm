import sys
sys.setrecursionlimit(100000)

N, R, Q = map(int, input().split())
connections = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().split())
    connections[U].append(V)
    connections[V].append(U)

counts = [0 for i in range(N+1)]

def make_node(curr_value: int):
    counts[curr_value] += 1
    for next_value in connections[curr_value]:
        if counts[next_value] == 0:
            counts[curr_value] += make_node(next_value)
    
    return counts[curr_value]

make_node(R)

for _ in range(Q):
    U = int(sys.stdin.readline())

    answer = counts[U]
    
    print(answer)
