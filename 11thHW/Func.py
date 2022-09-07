from sympy import *
from sympy.plotting import plot

x = Symbol('x')
f = -12*x**4*sin(cos(x))-18*x**3+5*x**2+10*x-30
plot(f)

