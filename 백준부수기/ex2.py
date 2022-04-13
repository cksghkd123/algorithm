import math


g = 9.806
pi = math.pi

h = float(input())
T = float(input())

w = 2*pi/T

x = (w**2)*h/g/math.sqrt(math.tanh((w**2)*h/g))
for i in range(1,21):
    fx = g*x/h*math.tanh(x)-w**2
    fxp = g/h*(math.tanh(x)+x/(math.cosh(x))**2)
    x = x-fx/fxp

k = x/h


