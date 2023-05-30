from partie1 import *



def log(n,p=6):
    sum=0
    for i in range(1,n+1):
        sum+=((-1)**(i+1))/i
    print(sum)
    sum=rp(sum,p)
    return sum

print(log(100000,10))

L = [math.log(1 + 10**(-k)) for k in range(7)]

A = [math.atan(10**(-k)) for k in range(10)]


def ln(x):
    k = 0
    y = 0
    p = 1
    while k <= 6:
        while x >= p + p * 10**(-k):
            y = y + L[k]
            p = p + p * 10**(-k)
        k = k + 1

    return y + (x/p - 1)

def exp(x):
    k = 0
    y = 1
    while k <= 6:
        while x >= L[k]:
            x = x - L[k]
            y = y + y * 10**(-k)
        k = k + 1
    return y + y * x

def arctan(x):
    if x==0 :
        return 0
    if x==1:
        return np.pi/4
    if x<0:
        return (-arctan(-x))
    elif x<1:
        return (np.pi/2-arctan(1/x))
    k = 0
    y = 1
    r = 0
    while k <= 4:
        while (x < y*10**(-k)):
            k = k+1
        xp = x-y*10**(-k)
        y = y+x*10**(-k)
        x = xp
        r += A[k]
    return (r+(x/y))

def tan(x):
    if x==0 :
        return 0
    if x<0 :
        return -tan(-x)
    if x >= np.pi :
        return tan(x%np.pi)
    if x > np.pi/2 :
        return -tan(np.pi -x) 
    if x > np.pi/4 :
        return 1/tan(np.pi/2 -x)
    k= 0
    m= 0
    d= 1       
    while (k <= 4):
        while (x >= A[k]) :
            x= x-A[k];                            
            mp= m+d*10**(-k)
            d= d-m*10**(-k)
            m= mp
        k= k+1
    return (m+x*d)/(d-x*m) 



X1=np.linspace(1,20,1000)
Y1=[ln(i) for i in X1]
Z1=np.log(X1)
#plt.subplot(2,2,1)
#plt.plot(X1,Y1,'y',label="ln_approx")
#plt.plot(X1,Z1,'g--',label="ln") 
#plt.legend()
#plt.title("Ln")
#plt.xlabel("x")
#plt.ylabel("ln(x)")

X2=np.linspace(-10,10,1000)
Y2=[exp(i) for i in X2]
Z2=np.exp(X2)
#plt.subplot(2,2,2)
#plt.plot(X2,Y2,'b',label="epx_approx")
#plt.plot(X2,Z2,'r--',label="exp")
#plt.legend()
#plt.title("Exp")
#plt.xlabel("x")
#plt.ylabel("exp(x)")

X3=np.linspace(-100,100,1000)
Y3=[arctan(i) for i in X3]
Z3=np.arctan(X3)
#plt.subplot(2,2,3)
#plt.plot(X3,Y3,'y',label="arctan_approx")
#plt.plot(X3,Z3,'g--',label="arctan")
#plt.legend()
#plt.title("Arctan")
#plt.xlabel("x")
#plt.ylabel("arctan(x)")


X4=np.linspace(-1.3,1.3,1000)
Y4=[tan(i) for i in X4]
Z4=np.tan(X4)
#plt.subplot(2,2,4)
#plt.plot(X4,Y4,'b',label="tan_approx")
#plt.plot(X4,Z4,'g--',label="tan")
#plt.legend()
#plt.title("Tan")
#plt.xlabel("x")
#plt.ylabel("tan(x)")
#
#plt.show()

W1=[abs((y-z)/z) for y,z in zip(Y1,Z1)]
plt.subplot(2,2,1)
plt.plot(X1,W1) 
plt.title("Erreur relative de Ln")
plt.xlabel("x")

W2=[abs((y-z)/z) for y,z in zip(Y2,Z2)]
plt.subplot(2,2,2)
plt.plot(X2,W2)
plt.title("Erreur relative de Exp")
plt.xlabel("x")

W3=[abs((y-z)/z) for y,z in zip(Y3,Z3)]
plt.subplot(2,2,3)
plt.plot(X3,W3)
plt.legend()
plt.title("Erreur relative de Arctan")
plt.xlabel("x")

W4=[abs((y-z)/z) for y,z in zip(Y4,Z4)]
plt.subplot(2,2,4)
plt.plot(X4,W4)
plt.legend()
plt.title("Erreur relative de Tan")
plt.xlabel("x")

plt.show()
