import math


n = int(input())
array = [True for i in range(n + 1)] 

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j=2
        while i*j <= n:
            array[i*j] = False
            j += 1

prime_numbers = []
for i in range(2, n + 1):
    if array[i]:
        prime_numbers.append(i)

pre_index = 0
post_index = 0
amount = 2

count = 0

while pre_index < len(prime_numbers):
    if amount < n:
        if post_index < len(prime_numbers)-1:
            post_index += 1
            amount += prime_numbers[post_index]
        else:
            amount -= prime_numbers[pre_index]
            pre_index += 1
    elif amount == n:
        count +=1
        amount -= prime_numbers[pre_index]
        pre_index += 1
    else:
        amount -= prime_numbers[pre_index]
        pre_index += 1


print(count)