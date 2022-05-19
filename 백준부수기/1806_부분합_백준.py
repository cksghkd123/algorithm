n, s = map(int,input().split())
numbers = list(map(int,input().split()))
pre_index = 0
post_index = 1
answer = 0
amount = numbers[0]

while pre_index < n:
    if pre_index < post_index:
        if amount >= s:
            if answer == 0:
                answer = post_index-pre_index
            else:
                answer = min(answer,post_index-pre_index)
            amount -= numbers[pre_index]
            pre_index += 1
        else:
            if post_index < n:
                amount += numbers[post_index]
                post_index += 1
            else:
                break
    else:
        amount += numbers[post_index]
        post_index += 1
    
print(answer)
        