n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
x = int(input())

num1 = 0
num2 = n-1
answer = 0

while num1 < num2:
    score = numbers[num1] + numbers[num2]

    if score == x:
        answer += 1
        num2 -= 1
    elif score < x:
        num1 += 1
    elif score > x:
        num2 -= 1

print(answer)
    