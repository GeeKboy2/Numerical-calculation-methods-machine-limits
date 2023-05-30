import math
import numpy as np
import matplotlib.pyplot as plt


def rp(x,p):
    signe = 1
    if x ==0:
        return 0
    if x<0:
        x*=-1
        signe =-1  
    n=0
    y=x
    chiffre = [i for i in range(1,10)]
    while int(y) not in chiffre :
        if y<1:
            y*=10 
            n+=1
        else :
            y/=10
            n-=1
    y =y*(10**p)
    if (y%10) >= 5:
        y+=(10-(y%10))
    else :
        y-=(y%10)
    y = int(y)/(10**(n+p))
    return signe*y

#tests
a =rp(10507.1823,4)
b =rp(10507.1823,6)
c =rp(0.0001857563,4)
d = rp(0.0001857563,6)
e = rp(3.141592658,4)
f = rp(3.141592658,6)


def machine_sum(x,y,precision=5) :
    return rp(x+y,precision)

def machine_multp(x,y,precision=5):
    return rp(x*y,precision)

def relative_error_sum(x,y):
    return abs((x+y) - machine_sum(x, y))/abs(x+y)

def relative_error_multp(x,y):
    return abs((x*y) - machine_multp(x, y))/abs(x*y)


def draw():
    x =0.0001857563
    X = np.linspace(-1,1,10**2)
    #erreur relative d'addition
    Y = [ relative_error_sum(x, y) for y in X ]
    plt.plot(X,Y,label="addition")

    #erreur relative de multiplication
    Z = [relative_error_multp(x, y) for y in X]
    plt.plot(X,Z,label="multiplication")

    plt.legend()
    plt.show()


#décommenter pour visualiser
#draw()