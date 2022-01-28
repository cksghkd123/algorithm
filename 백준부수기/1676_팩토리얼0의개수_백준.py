n = int(input())

fiveCount= 0
twoCount= 0

twos= 2
fives= 5
while(twos<= n):
    twoCount += n//twos
    twos*= 2

while(fives<= n):
    fiveCount += n//fives
    fives*= 5

result= min(twoCount, fiveCount)
print(result)


    