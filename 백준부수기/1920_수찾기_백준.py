def bia_search(target, left, right):
    if  left <= right:
        mid = (left+right)//2

        if target < first_list[mid]:
            return bia_search(target, left, mid-1)
        elif target == first_list[mid]:
            return 1
        else:
            return bia_search(target, mid+1, right)

    else:
        return 0
        


n = int(input())
first_list = sorted(map(int,input().split()))
m = int(input())
search_list = map(int,input().split())
for i in search_list:
    result = bia_search(i, 0, len(first_list)-1)
    print(result)