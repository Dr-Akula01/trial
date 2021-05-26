from numpy import exp
import matplotlib.pyplot as plt



def f(x,y):
    return x+y

xcoord=[]
ycoord=[]

def EC(f,x0,y0,xn,h):
    for _ in range(100):
        y = y0 + h*f(x0,y0)
        #print(y)
        y0=y
        x0=x0+h
        xcoord.append(x0)
        ycoord.append(y0)

EC(f,x0=0,y0=1,xn=1,h=0.08)

func=2*exp(xcoord)-xcoord-1

print(xcoord)
print(ycoord)

plt.plot(xcoord,ycoord, label='EC')
plt.plot(xcoord,func, label='exact')
plt.legend()
plt.show()


