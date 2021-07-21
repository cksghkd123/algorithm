def permutation(list, r, result):
    if len(result) == r:
        print(' '.join(map(str,result)))
        return
    
    for i in list:
        permutation(list, r, result + [i])

n, m = map(int,input().split())
nn = [i+1 for i in range(n)]
permutation(nn, m, [])