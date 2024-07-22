D = int(input())
N = 8

connections = [[0 for _ in range(N)] for _ in range(N)]

nodes = [(0,1), (0,2), (1,0), (1,2), (1,3), (2,0), (2,1), (2,3), (2,4), (3,1), (3,2), (3,4), (3,5), (4,2), (4,3), (4,5), (4,7), (5,3), (5,4), (5,6), (6,5), (6,7), (7,4), (7,6)]

for a, b in nodes:
    connections[a][b] = 1

def calculate(n):
    if n not in memo:
        new_list = [[0 for _ in range(N)] for _ in range(N)]
        a_list = calculate(n//2)
        b_list = calculate(n-n//2)

        for i in range(N):
            for j in range(N):
                for k in range(N):
                    new_list[i][j] += a_list[i][k] * b_list[k][j]
                new_list[i][j] %= 1000000007

        memo[n] = new_list
    
    return memo[n]

memo = {}
memo[1] = connections

result = calculate(D)

print(result[0][0])