def combination(list , r, k, result):
    if len(result) == r:
        print(' '.join(map(str,result)))    
        return

    if k > len(list):
        return

    combination(list, r, k+1, result + [k])
    combination(list, r, k+1, result)

n, m = map(int,input().split())
nn = [i+1 for i in range(n)]
combination(nn, m, 1, [])
