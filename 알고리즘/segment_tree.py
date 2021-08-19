#초기값

array = [1,2,3,4,5,6,7,8,9,10]
# <<트리의 크기>>
# 2^k 로 N보다 바로 큰 값을 만드는 k >> 2^4 = 16 > 10
# 배열의 크기 2^(k+1) >> 2^5 = 32
tree = [0]*(len(array)*4) # N*4로 완전이진트리로 한다하고 편하게 트리의 크기를 정했음
                          # 새그먼트 트리의 크기는 배열(arr)의 개수가 N개일 때, 
                          # N보다 큰 가장 가까운 N의 제곱수를 구한 뒤에 그것의 2배를 하여 미리 세그먼트 트리의 크기를 만들어놓어야 한다.


def init(start, end, index):
    if start == end: #가장 끝에 도달 했으면 array 삽입
        tree[index] = array[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
    #좌측 노드와 우측 노드를 합한다
    return tree[index]
    #리턴

def query(start, end, index, qleft, qright):
    #주어진 범위가 전체 범위를 벗어나는 경우
    if qleft > end or qright < start:
        return 0 # 리턴
    #주어진 범위가 전체 범위를 완전히 포함하는 경우
    if qleft <= start and end <= qright:
        return tree[index]
    
    mid = (start + end) // 2
    return query(start, mid, index*2, qleft, qright) + query(mid+1, end, index*2+1, qleft, qright)
    #주어진 범위가 걸쳐있는 경우

def update(start, end, index, what, value):
    # 범위 밖에 있는 경우
    if what < start or what > end:
        return
    # 범위 안에 있으면 내려가면서 다른 원소도 갱신
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)

init(0, len(array), 1) 
#인덱스 1부터 시작 >> 1부터 해야 왼쪽 노드를 짝수로 정렬이 가능하기 편해서
#세그먼트 트리의 인덱스가 1번부터 시작하는 이유는 재귀적으로 편하게 세그먼트 트리를 생성하기 위해서이다. 
#1부터 시작하게 되면 2를 곱했을 때는 왼쪽 자식 노드를 가리키고, 
# 2를 곱하고 1을 더하면 오른쪽 자식 노드를 가리키게 되어 효과적이기 때문이다.
s, e = map(int,input().split()) # 구간선택
result = query(0, len(array), 1, s, e)
print(result)


##반복문으로 구간의 합 >> O(N)의 시간복잡도
##새그먼트 트리로 구간의 합  >> O(logN)으이 시간복잡도

