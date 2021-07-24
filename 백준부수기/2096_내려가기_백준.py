def max_drop(a, b):
    c = [ max(a[0], a[1]) + b[0], max(a) + b[1], max(a[1], a[2]) + b[2] ]
    return c

def min_drop(a, b):
    c = [ min(a[0], a[1]) + b[0], min(a) + b[1], min(a[1], a[2]) + b[2] ]
    return c


n = int(input())
max_result = [0, 0, 0]
min_result = [0, 0, 0]

for _ in range(n):
    floor_list = list(map(int,input().split()))
    max_result = max_drop(max_result, floor_list)
    min_result = min_drop(min_result, floor_list)

print(max(max_result), min(min_result))


    