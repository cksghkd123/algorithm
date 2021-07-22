def ppprint(list):
    for i in list:
        print(i,end=' ')
    print('')

def permutation(list, r, result):
    if len(result) == r:
        ppprint(result)

    for i in list:
        if visited[i] == False:
            visited[i] = True
            permutation(list, r, result + [i])
            visited[i] = False


n, m = map(int,input().split())
nn = [i+1 for i in range(n)]
visited = [False for _ in range(n+1)]
permutation(nn, m, [])