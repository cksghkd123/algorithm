def holjjak(x):
    if x/2 == int(x/2):
        return 0
    else:
        return 1

def fireball_move(row,col,mas,spd,dir):
    w = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    
    nr, nc = (y + z for y,z in zip((row, col) , (map(lambda x: x*spd, w[dir]))))
    while 0 < nr or N <= nr:
        if nr < 0:
            nr += N
        elif nr >= N:
            nr -= N

    while 0 < nc or N <= nc:
        if nc < 0:
            nc += N
        elif nc >= N:
            nc -= N
    
    
    
    print(nr,nc)

    

def fireball_check():
    list = {}
    for i in range(len(fireball_info)):
        list[(fireball_info[i][0],fireball_info[i][1])] = []
    
    for i in range(len(fireball_info)):
        list[(fireball_info[i][0],fireball_info[i][1])].append(i)

    list2 = []

    for n in list.values():
        if len(n) > 1:
            list2.append(n)
        
    return list2

def fireball_crash():
    for i in range(len(com_fireball)):
        nm = 0
        ns = 0
        for n in com_fireball[i]:
            nm += fireball_info[n][2]
            ns += fireball_info[n][3]
            if n == 0:
                hj = holjjak(fireball_info[n][4])
                nd = 0
            else:
                if nd == 0:
                    if holjjak(fireball_info[n][4]) != hj:
                        nd = 1
        
        for n in reversed(om_fireball[i]):
            fireball_info.pop(n)

        nm = int(nm/5)
        if nm == 0 :
            continue
        
        ns = int(ns/len(com_fireball[i]))

        if nd == 0:
            for i in range(4):
                fireball_info.append(com_fireball[0],com_fireball[1],nm,ns,i*2)
        elif nd == 1:
            for i in range(4):
                fireball_info.append(com_fireball[0],com_fireball[1],nm,ns,i*2+1)

def fireball_mass():
    total = 0
    for n in fireball_info:
        total += n[2]
    print(total)
    
N, M, K = map(int,input().split())
fireball_info = [list(map(int,input().split())) for _ in range(M)]




for _ in range(K):

    for f in fireball_info:
        fireball_move(f[0],f[1],f[2],f[3],f[4])

    com_fireball = fireball_check()

    fireball_crash()

fireball_mass()





    
    