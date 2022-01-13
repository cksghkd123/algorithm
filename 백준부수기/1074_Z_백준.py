n, r, c = list(map(int, input().split()))

def ZZ():
    number_range = [0,2**(2*n)-1]
    quarter_volume = 2**(2*n)//4
    nn = n
    row = 0
    col = 0
    while number_range[0] != number_range[1]:
        half_number = (2**nn)//2
        if r < row+half_number:
            if c < col+half_number:
                number_range[1] = number_range[0] + quarter_volume -1
            else:
                number_range[0] = number_range[0] + quarter_volume
                number_range[1] = number_range[0] + quarter_volume -1
                col += half_number
        else:
            if c < col+half_number:
                number_range[0] = number_range[0] + 2*quarter_volume
                number_range[1] = number_range[0] + quarter_volume -1
                row += half_number
            else:
                number_range[0] = number_range[0] + 3*quarter_volume
                number_range[1] = number_range[0] + quarter_volume -1
                row += half_number
                col += half_number

        quarter_volume = quarter_volume // 4
        nn -= 1
    return number_range[0]

if r == 0 and c == 0:
    answer = 0
else:
    answer = ZZ()

print(answer)