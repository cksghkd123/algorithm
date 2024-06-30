def combination(n, m, array, result):
    if len(result) == m:
        if str(result) not in printed:
            printed.add(str(result))
            print(*result) 
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            combination(n, m, array, result + [array[i]])
            visited[i] = False



N, M = map(int, input().split())
number_list = list(map(int, input().split()))
printed = set()

number_list.sort()

visited = [False for _ in range(N)]
combination(N, M, number_list, [])
