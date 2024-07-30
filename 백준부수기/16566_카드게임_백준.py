from bisect import bisect_right

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootX] = rootY

N, M, K = map(int, input().split())

card_list = list(map(int, input().split()))
k_list = list(map(int, input().split()))

card_list.sort()

parent = list(range(M+1))

for k in k_list:
    idx = bisect_right(card_list, k)
    if idx == M or find(idx) == M:
        print(card_list[M-1])
        union(idx, idx+1)
    else:
        chosen_card = card_list[find(idx)]
        print(chosen_card)
        union(find(idx), find(idx)+1)
    