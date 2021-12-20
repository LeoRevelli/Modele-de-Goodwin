# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 16:12:46 2021

@author: leore
"""
import pylab
alpha=0.02
delta=0.01
beta=0.03
v=10
N=50000
K=20000
a=15
L=K/(a*v)
w=1
Y=K/v
omega=w/a
Lambda=L/N
OMEGA=[omega]
LAMBDA=[Lambda]
prod=[Y]
t=0
T=[t]
while t<1000:
    N=N+beta*N
    K=K+Y-w*L
    a=a+beta*a
    L=K/(a*v)
    Lambda=L/N
    w=w+2*Lambda*w
    Y=K/v
    prod=prod+[Y/(a*N)]
    omega=w/a
    OMEGA=OMEGA+[omega]
    LAMBDA=LAMBDA+[Lambda]
    PROD=[prod]
    t=t+1
    T=T+[T]
print (OMEGA)
print (LAMBDA)
#pylab.plot(OMEGA,LAMBDA)
pylab.plot(T,prod)