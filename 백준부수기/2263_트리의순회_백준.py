import sys
sys.setrecursionlimit(10**9)

def preorder(in_start, in_end, post_start, post_end):
    # 재귀 종료 조건 (수렴)
    if(in_start > in_end) or (post_start > post_end):
        return

    # 후위 순회 결과의 끝이 (서브)트리의 루트임을 이용
    parents = postorder[post_end]

    # 중위 순회에서 루트의 좌 우로 자식들이 갈라지는 것을 이용하여 left, right를 선언
    left = position[parents] - in_start
    right = in_end - position[parents]

    # left, right로 나눠 분할 정복 방식으로 트리를 추적하여 전위 순회를 찾아냄
    print(parents, end=" ")
    preorder(in_start, in_start+left-1, post_start, post_start+left-1) # 왼쪽 서브트리
    preorder(in_end-right+1, in_end, post_end-right, post_end-1) # 오른쪽 서브트리


n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 후위 순회의 끝값이 중위 순회의 어디 인덱스에 위치한지 확인을 위해
# 중위 순회의 값들의 인덱스값을 저장
position = [0]*(n+1)
for i in range(n):
    position[inorder[i]] = i

# 중위 순회, 후위 순회 모두 0부터 n-1 (전체 범위)값을 주고 전위 순회를 구함
preorder(0, n-1, 0, n-1)
