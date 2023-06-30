import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure
import scipy.integrate as integrate
from itertools import cycle
import sys


fig = figure(figsize=(12, 7), dpi=120)


def periodicf(li,lf,f,x):
    if x>=li and x<=lf :
        return f(x)
    elif x>lf:
        x_new=x-(lf-li)
        return periodicf(li,lf,f,x_new)
    elif x<(li):
        x_new=x+(lf-li)
        return periodicf(li,lf,f,x_new)

def functionP(li,lf,x):
    return periodicf(li,lf,function,x)

def function(x):
    return 2*x

def fourierCoeffs(li, lf, n, f):
    l = (lf-li)/2
    # Constant term
    a0=1/l*integrate.quad(lambda x: f(x), li, lf)[0]
    # Cosin coefficents
    A = np.zeros((n))
    # Sin coefficents
    B = np.zeros((n))
     
    for i in range(1,n+1):
        A[i-1]=1/l*integrate.quad(lambda x: f(x)*np.cos(i*np.pi*x/l), li, lf)[0]
        B[i-1]=1/l*integrate.quad(lambda x: f(x)*np.sin(i*np.pi*x/l), li, lf)[0]
 
    return [a0/2.0, A, B]

def fourierSeries(coeffs,x,l,n):
    value = coeffs[0]
    for i in range(1,n+1):
        value = value + coeffs[1][i-1]*np.cos(i*np.pi*x/l) +  coeffs[2][i-1]*np.sin(i*np.pi*x/l)
    return value
     


#main

li = -np.pi
lf = np.pi
l = (lf-li)/2.0
n = 1

cycol = cycle('bgrcmk')

for n in range(1,10):
    plt.title('Fourier Series Approximation\nSawtooth Wave\n n = '+str(n))

    coeffs = fourierCoeffs(li,lf,n,function)
    step_size = 0.2
    x_l = -np.pi*2
    x_u = np.pi*2

    x = np.arange(x_l,x_u,step_size)
    y = [functionP(li,lf,xi) for xi in x]
    y_fourier = [fourierSeries(coeffs,xi,l,n) for xi in x]
        
    x_plot =[]
    y_plot = []
    y_plot_fourier = []
        
    x_l_plot = x_l - 13
    x_u_plot = x_l + 1
    plt.xlim(x_l_plot,x_u_plot)
    plt.ylim(-10,10)

    j = next(cycol)
    for i in range(x.size): 
        x_plot.append(x[i])
        y_plot.append(y[i])
        y_plot_fourier.append(y_fourier[i])
        
        plt.plot(x_plot,y_plot,c='darkkhaki',label='Function')
        plt.plot(x_plot,y_plot_fourier,c=j,label='Fourier Approximation')
        
        x_l_plot = x_l_plot + step_size
        x_u_plot = x_u_plot + step_size
        plt.xlim(x_l_plot,x_u_plot)
        plt.pause(0.001)
        
        if not plt.get_fignums():
            sys.exit()
    
plt.show()