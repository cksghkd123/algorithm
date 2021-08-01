def bin_search(target, left, right):
    if left <= right:
        mid = (left + right)//2

        if target < card_list[mid]:
            return bin_search(target, left, mid-1)
        elif target > card_list[mid]:
            return bin_search(target, mid+1, right)
        else:
            return how_many(mid)
    
    else:
        return 0

def how_many(card_index):
    card = card_list[card_index]
    count = 0
    w = [1,-1]
    for dw in w:
        index = card_index
        while 1:
            if 0 <= index < limit and card_list[index] == card:
                count += 1
                index += dw
            else:
                break
    
    return count-1


n = int(input())
card_list = list(sorted(map(int,input().split())))
m = int(input())
sellect_card = list(map(int,input().split()))
result = []
limit = len(card_list)

for i in sellect_card:
    result.append(bin_search(i, 0, limit-1))
print(*result)