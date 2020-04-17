from math import sin, cos, sqrt, pi
from functools import reduce

from matplotlib import pyplot as plt

A = [0.5, 1, 2]
G = 9.81
OMEGA = sqrt(G)

def getF(a):
    def f(t, fi):
        return -G*sin(fi) + a*sin(OMEGA*t)*cos(fi)
    
    return f

def solution(f, n):
    step = 30/n
    prev_t = t = 0
    prev_z = z = 0
    prev_fi = fi = 0

    result = [(t, fi)]

    for i in range(1, n+1):
        t = prev_t + step

        temp_z = prev_z + step*f(prev_t, prev_fi)
        temp_fi = prev_fi + step*prev_z

        z = prev_z + step*(f(prev_t, prev_fi) + f(t, temp_fi))/2
        fi = prev_fi + step*(prev_z + temp_z)/2

        prev_t = t
        prev_z = z
        prev_fi = fi
        result.append((t, fi))
    
    return result


for a in A:
    result = []
    f = getF(a)
    n = 2

    while(True):
        fi1 = solution(f, n)
        fi2 = solution(f, 2*n)

        alpha = abs(fi1[-1][1] - fi2[-1][1])/3

        if 2*abs(1-cos(alpha)) < 0.001:
            result = fi2
            break

        n = 2*n
    

    x, y = [], []
    for point in result:
        x.append(point[0])
        y.append(point[1])

    plt.plot(x, y)
    print (
        f'A = {a}\n'
        f'|Fi_max| = {reduce(lambda acc, val: abs(val) if abs(val) > acc else acc, y, abs(y[0])):5.2f}'
    )
    plt.show()
