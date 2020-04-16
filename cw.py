from math import sin, cos, sqrt

A = 1
G = 9.81
OMEGA = sqrt(G)
EPS = 10**(-5)

def f(t, fi):
    return -G*sin(fi) + A*sin(OMEGA*t)*cos(fi)

def solution(n):
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

n = 2

while(True):
    y_1 = solution(n)[-1][1]
    y_2 = solution(2*n)[-1][1]

    if abs(y_1 - y_2)/3 < EPS:
        print(y_2)
        break
    n = 2*n
