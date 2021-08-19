#초기값

array = [1,2,3,4,5,6,7,8,9,10]
# <<트리의 크기>>
# 2^k 로 N보다 바로 큰 값을 만드는 k >> 2^4 = 16 > 10
# 배열의 크기 2^(k+1) >> 2^5 = 32
tree = [0]*(len(array)*4) # N*4로 완전이진트리로 한다하고 편하게 트리의 크기를 정했음

def init(start, end, index):
    if start == end: #가장 끝에 도달 했으면 array 삽입
        tree[index] = array[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
    #좌측 노드와 우측 노드를 합한다

def query(start, end, index, qleft, qright):
    #주어진 범위가 전체 범위를 벗어나는 경우
    if qleft > end or qright < start:
        return 0 # 리턴
    #주어진 범위가 전체 범위를 완전히 포함하는 경우
    if qleft <= start and end <= qright:
        return tree[index]
    
    mid = (start + end) // 2
    return query(start, mid, index*2, qleft, qright) + query(mid+1, end, index*2+1, qleft, qright)


init(1, len(array), 1) #인덱스 1부터 시작 >> 1부터 해야 왼쪽 노드를 짝수로 정렬이 가능하기 편해서
s, e = map(int,input().split()) # 구간선택
result = query(1, len(array), 1, s, e)
print(result)

##반복문으로 구간의 합 >> O(N)의 시간복잡도
##새그먼트 트리로 구간의 합  >> O(logN)으이 시간복잡도

