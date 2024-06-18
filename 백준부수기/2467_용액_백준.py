n = int(input())

liquid_list = list(map(int, input().split()))

result = float('inf')
left = 0
right = n-1
answer = [liquid_list[0], liquid_list[n-1]]

while left < right:
    dif = abs(liquid_list[right] + liquid_list[left])
    if dif < result:
        answer = [liquid_list[left], liquid_list[right]]
        result = dif
    
    if liquid_list[left] + liquid_list[right] < 0:
        left += 1
    else:
        right -= 1
    
for a in answer:
    print(a)

