def binary_search(target, left, right):
    if  left <= right:
        mid = (left+right)//2

        if target < first_list[mid]:
            return binary_search(target, left, mid-1)
        elif target == first_list[mid]:
            return mid # 찾았을 때
        else:
            return binary_search(target, mid+1, right)

    else:
        return -1 # 못찾았을 때

#탐색을 할 리스트를 정렬을 하고 검색해야한다.
first_list = [2,3,7,1,4,9]
first_list.sort()

x = input()
result = binary_search(x, 0, len(first_list)-1)