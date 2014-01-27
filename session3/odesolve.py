# odesolve.py

from pylab import *
from scipy.integrate import odeint

# odeint is an LSODA based ODE solver

# Define the function:
def f(y, t0):
    return -2*y**2;

# Initial condition:
y0 = 3

# Solve for some `t':
t = linspace(0, 5, 100)
y = odeint(f, y0, t)

plot(t,y)
xlabel('t'); ylabel('y'); title(r"$\frac{dy}{dt}=-2y^2$") # You can use LaTeX with Matplotlib like this!
savefig('solution.png')
show()
