#원래 visited 한칸에는 T,F 두가지의 경우지만 이는 상태를 저장한다
#많은 상태를 저장하기에는(메모리 효율) 비트마스킹이 매우 효율적이다
x = 5 #예상하는 상태 개수
visited = [[[0]*(2**x) for _ in range(m)] for _ in range(n)]

index = 24

# &는 and 명령문 같은 비트만 1을 출력
result = index & (1 << (ord('D') - ord('A'))) # D - A 의 아스키코드 값으로 수치화해서 비트로 찍어냄 
# |는 or 명령문 둘중 하나라도 1이면 1을 출력
result = index | (1 << (ord('d')- ord('a')))

#그 상태값에 대한 visited를 변환시킴
visited[row][col][index] = 1
    