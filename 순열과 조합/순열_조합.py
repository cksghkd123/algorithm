list = [1,2,3,4]

#순열
visit = [False for _ in range(len(list))]

def permutation(n,result):
    if len(result) == n:
        print(result)
        return
    
    else:
        for i in range(len(list)):
            if visit[i] == False:
                visit[i] = True
                permutation(n,result + [list[i]])
                visit[i] = False

##permutation(r,[])

#중복순열
visit = [False for _ in range(len(list))]

def permutation_ov(n,result):
    if len(result) == n:
        print(result)
        return 
    
    else:
        for i in range(len(list)):
            permutation_ov(n,result + [list[i]])

##permutation_ov(r, [])

#조합
def combination(k, r, result):
    if len(result) == r:
        print(result)
        return
    if k >= len(list):
        return
    else:
        combination(k+1, r, result + [list[k]])
        combination(k+1, r, result)

##combination(0, r, [])

#중복조합
def combination_ov(k, r, index, result):
    if len(result) == r:
        print(result)
        return

    for i in range(index, len(list)):
        combination_ov(k+1, r, i, result + [list[i]])

##combination_ov(0, r, 0, [])
