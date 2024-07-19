import sys
sys.setrecursionlimit(10**6)

def lower_bound_binary_search(arr, n):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left+right) // 2
        
        if arr[mid] < n:
            left = mid + 1
        else:
            right = mid
    return left

input_list = []

while True:
    try:
        input_value = int(input())
        input_list.append(input_value)
    except:
        break

def pre_to_post_order(preorder_list):
    if len(preorder_list) == 0:
        return
    
    i = lower_bound_binary_search(preorder_list[1:], preorder_list[0])
    pre_to_post_order(preorder_list[1:1+i])
    pre_to_post_order(preorder_list[1+i:])
    
    print(preorder_list[0])


pre_to_post_order(input_list)