# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 16:02:13 2021

@author: leore
"""
import pylab
alpha=0.5
delta=0.01
beta=0.6
v=10
omega=0.3
Lambda=0.4
OMEGA=[omega]
LAMBDA=[Lambda]
t=0
T=[t]
while t<100:
    omega=omega+omega*(2*Lambda-alpha) #omega t+1
    Lambda=Lambda+Lambda*(((1-omega)/v-delta)-alpha-beta)
    OMEGA=OMEGA+[omega]
    LAMBDA=LAMBDA+[Lambda]
    t=t+1
    T=T+[t]
print(OMEGA)
pylab.plot(LAMBDA,OMEGA)