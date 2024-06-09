import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

cur = 0
count = 0
result = 0

while cur < (m - 1):
    if s[cur:cur + 3] == 'IOI': # P_1 으로 체크
        count += 1
        cur += 2
        if count == n:      # P_1이 n개가 되면 
            result += 1     # P_n 갯수 증가
            count -= 1
    else:
        # cur부터 3개의 문자가 IOI 가 아니면 P_1 갯수 초기화
        count = 0
        cur += 1

print(result)