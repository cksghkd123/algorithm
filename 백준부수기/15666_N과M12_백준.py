def solution(n, m, number_list, k, result):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(k, n):
        solution(n, m, number_list, i, result+[number_list[i]])


N, M = map(int, input().split())

numbers = list(set(map(int, input().split())))
numbers.sort()

solution(len(numbers), M, numbers, 0, [])
