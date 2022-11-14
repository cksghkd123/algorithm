#zip
for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    print(number, upper, lower)

##실전##2차원 배열의 row, col 대입
number = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
n_number = [list(i) for i in zip(*reversed(number))]
print(n_number)


#unzip
numbers = (1, 2, 3)
letters = ("A", "B", "C")
pairs = list(zip(numbers, letters))
# pairs = [(1, 'A'), (2, 'B'), (3, 'C')]
numbers, letters = zip(*pairs)
print(numbers)
print(letters)

#dictionary
keys = [1, 2, 3]
values = ["A", "B", "C"]
print(dict(zip(keys, values)))
# {1: 'A', 2: 'B', 3: 'C'}