def init(start, end, index):
    if start == end:
        tree[index] = array[start]
        return tree[index]
    mid = (start + end)//2
    tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
    return tree[index]

def query(start, end, index, left, right):
    if left > end or right < start:
        return 0
    elif left <= start and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    return query(start, mid, index*2, left, right) + query(mid+1, end, index*2+1, left, right)

def update(start, end, index, what, value):
    if what < start or what > end:
        return
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)


n, m, k = map(int,input().split())
array = []
for _ in range(n):
    array.append(int(input()))

tree = [0]*(len(array)*4)
init(0, n-1, 1)
for _ in range(m+k):
    a, b, c = map(int,input().split())
    if a == 1:
        change = c - array[b-1]
        array[b-1] = c
        update(0, n-1, 1, b-1, change)
    elif a == 2:
        result = query(0, n-1, 1, b-1, c-1)
        print(result)
