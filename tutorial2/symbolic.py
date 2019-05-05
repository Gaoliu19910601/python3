import sympy as sym

x = sym.Symbol('x')
y = sym.Symbol('y')

print(sym.integrate(x**2+x+1))
print(sym.integrate(x**2+sym.sin(x)))
print(sym.expand((x+y)**3))
print(sym.solve(x**4 - 1 , x))
print(sym.factor(x**4-3*x**2+1))

l = sym.Symbol('l')
T = sym.Symbol('T')

print(sym.integrate(sym.sin(2*sym.pi*l/T),l))

from sympy.integrals import laplace_transform as lt
from sympy.abc import t,s

a = lt(t**2+t+1,t,s)

print(a)

from sympy.integrals import inverse_laplace_transform as ilt

b = ilt((s**2+s+2)/(s**3),s,t)
print(b)