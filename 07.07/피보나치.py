#fibo1 재귀방법
def fibo(n):
    n -= 1
    if n < 2:
        return 1
    return fibo(n-1) + fibo(n-2)


#fibo2 for문
def fibo2(n):
    if n < 2:
        return 1
    a ,b = 0 ,1
    for i in range(n-1):
        a,b = b,a+b # swap 코드

    return b


#fibo3 memoization
fibo_list = [0 for _ in range(100)]
fibo_list[1] = 1
for i in range(2,len(fibo_list),1):
    fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
