def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    
    return root[x]

def union(x, y):
    fx = find(x)
    fy = find(y)

    if fx != fy:
        root[x] = y
         

G = int(input())
P = int(input())

plane_info_list =[]

for _ in range(P):
    plane_info_list.append(int(input()))

answer = 0

root = [i for i in range(G+1)]

for plane in plane_info_list:
    r = find(plane)
    if r == 0:
        break
    union(r, r - 1)
    answer += 1
    
print(answer)
        
