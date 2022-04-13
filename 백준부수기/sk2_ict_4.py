def solution(n, m, k, records):
    INF = float('inf')
    relations = [[INF for _ in range(m)] for _ in range(k)]
    for record in records:
        for i in range(k):
            for j in range(k):
                if i == j:
                    relations[i][j] = 0
                if abs(relations[i][j]) > abs(record[j] - record[i]):
                    relations[i][j] = record[j]-record[i]

    answer = [m, m, m, m]
    for i in range(k):
        for j in range(i+1, k):
            relations[i][j]
        print(relations)
    
    
print(solution(8,4,4,[[1, 5, 1, 3], [5, 7, 5, 6]]))
print(solution(8,4,4,[[5, 1, 1, 3], [7, 5, 5, 6]]))

print(solution(8,4,4,[[1, 5, 1, 3], [1,5,1,2]]))

print(solution(10,3,3,[[1, 2, 3], [5, 7, 10]]))
    




# 8	4	4	[[1, 5, 1, 3], [5, 7, 5, 6]]	
# [1, 3, 1, 2]
# 8	4	4	[[1, 5, 1, 3]]	            
# [1, 4, 1, 3]
# 10 3	3	[[1, 2, 3], [5, 7, 10]]	
# [1, 2, 3]