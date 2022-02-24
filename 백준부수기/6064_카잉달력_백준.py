def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def lcm(x, y):
    result = (x*y)//gcd(x,y)
    return result

t = int(input())

for _ in range(t):
    m, n, x, y = map(int,input().split())
    limit = lcm(m,n)
    number = x
    answer = -1
    while number <= limit:
        if y == n:
            if number%n == 0 :
                answer = number
                break
        else:
            if number%n == y:
                answer = number
                break

        number += m
    
    print(answer)
        
