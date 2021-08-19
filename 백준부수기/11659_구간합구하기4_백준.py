# n, m = map(int,input().split())
# arr = list(map(int,input().split()))

# prefix_sum = [0]
# total = 0

# for i in arr:
#     total += i
#     prefix_sum.append(total)

# for _ in range(m):
#     s, e = map(int,input().split())
#     result = prefix_sum[e] - prefix_sum[s-1]
#     print(result)

n, m = map(int,input().split())
arr = list(map(int,input().split()))

prefix_sum = [0]*(n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]

for _ in range(m):
    s, e = map(int,input().split())
    result = prefix_sum[e] - prefix_sum[s-1]
    print(result)
