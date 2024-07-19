A, B = map(int, input().split())

def binary(n):
    if n == 1 or n == 0:
        return str(n)
    
    return binary(n//2) + str(n%2)


b_a = binary(A-1)
b_b = binary(B)
dp = [0 for _ in range(len(b_b)+1)]
#dp[i] = '2^i까지 1의 개수'
dp[0] = 1
dp[1] = 2
for i in range(2, len(b_b)):
    dp[i] = 2* (dp[i-1]-1) + 2**(i-1) + 1

def get_one_counts(binary_n):
    result = 0
    one_count = 0
    for i in range(len(binary_n)):
        point = len(binary_n)-1-i
        if binary_n[i] == '1':
            result += dp[point]
            result += one_count*(2**point)
            one_count += 1

    return result

answer = get_one_counts(b_b) - get_one_counts(b_a)

print(answer)

# 0000
# 0001
# 0010
# 0011
# 0100
# 0101
# 0110
# 0111
# 1000
# 1001
# 1010
# 1011
# 1100

