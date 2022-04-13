import math


g = 9.806
pi = math.pi

h_array = [0.2, 0.5, 1, 5, 10, 20, 50, 100, 200, 1000]
T = 10

w = 2*pi/T
L_disperation = []
L_Eckart = []
iteration_time = []
min_dif = 0.0000000001              #이만큼 오차가 날 때 수렴한다고 가정한다.

for h in h_array:
    x = (w**2)*h/g/math.sqrt(math.tanh((w**2)*h/g))
    L_Eckart.append(x)
    for i in range(1,21):
        fx = g*x/h*math.tanh(x)-w**2
        fxp = g/h*(math.tanh(x)+x/(math.cosh(x))**2)
        new_x = x-fx/fxp
        if new_x-x < min_dif:
            break
        else:
            x = new_x

    L_disperation.append(x)
    iteration_time.append(i)

L_approx = [None,float('inf')]

print("==========결과==========")
for i in range(len(h_array)):
    print("h = {}m, T = 10".format(h_array[i]))
    print("분산법 L = {}".format(L_disperation[i]))
    print("Eckart L = {}".format(L_Eckart[i]))
    print("수렴할 때까지 반복횟수: {}".format(iteration_time[i]))
    if abs(L_approx[1]-1) > abs(L_disperation[i]-1):
        L_approx = [h_array[i], L_disperation[i]]

print("L=1m 와 가장 가까울 때 h = {}".format(L_approx[0]))