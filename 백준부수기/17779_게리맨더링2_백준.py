def population_check(n1, n2, n3, n4):
    population = [0 for _ in range(5)]
    for row in range(n):
        for col in range(n):
            if 0 <= row < n1[0] and 0 <= col <= n2[1] and row+col < sum(n1):
                population[0] += map_list[row][col]
            elif 0 <= row <= n4[0] and n2[1] < col < n and col-row > n2[1]-n2[0]:
                population[1] += map_list[row][col]
            elif n1[0] <= row < n and 0 <= col < n3[1] and col-row < n3[1]-n3[0]:
                population[2] += map_list[row][col]
            elif n4[0] < row < n and n3[1] <= col < n and row+col > sum(n4):
                population[3] += map_list[row][col]
            else:
                population[4] += map_list[row][col]
    difference = max(population) - min(population)
    return difference


n = int(input())
map_list = [list(map(int,input().split())) for _ in range(n)]
answer = float('inf')
for row in range(n):
    for col in range(n):
        for d2 in range(1, n):
            for d1 in range(1,n):
                if 0 <= row+d1+d2 < n and 0 <= col-d1 < col+d2 < n:
                    result = population_check((row+d1, col-d1), (row,col), (row+d1+d2, col-d1+d2) , (row+d2, col+d2))
                    answer = min(answer, result)
                else:
                    break
            if d1 == 1:
                break
        
print(answer)