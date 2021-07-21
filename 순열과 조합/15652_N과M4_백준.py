def combination(list, r, index, result):
    if len(result) == r:
        print(' '.join(map(str,result)))
        return
    
    for i in range(index, len(list)):
        combination(list, r, i, result + [list[i]])

n, m = map(int,input().split())
nn = [i+1 for i in range(n)]
combination(nn, m, 0, [])