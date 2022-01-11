fibo_list = {0:(1,0), 1:(0,1)}

def fibofibo(n: int):
    if n in fibo_list:
        return fibo_list[n]
    else:
        a = fibofibo(n-1)
        if (n-1) not in fibo_list:
            fibo_list[n-1] = a
        b = fibofibo(n-2)
        return tuple(map(lambda x,y: x+ y, a,b))

T = int(input())


for i in range(T):
    result = fibofibo(int(input()))
    print(result[0], result[1])