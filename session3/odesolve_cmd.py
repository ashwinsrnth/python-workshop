# odesolve_cmd.py

import sys
from pylab import *
from scipy.integrate import odeint

# odeint is an LSODA based ODE solver

# Define the function:
def f(y, t0):
    return -2*y**2;

# Initial condition:

# The 'sys' module (imported above), contains
# objects that are related to the python interpreter.

# The command line arguments are stored in
# a list 'sys.argv'.
# sys.argv[0] is always the name of the program.
# sys.argv[1] is the first command line argument.
# sys.argv[2] is the second .. and so on

# Since we only have one command line argument,
# (the initial condition):

y0 = float(sys.argv[1])
# Solve for some `t':
t = linspace(0, 5, 100)
y = odeint(f, y0, t)

plot(t,y)
xlabel('t'); ylabel('y'); title(r"$\frac{dy}{dt}=-2y^2$") # You can use LaTeX with Matplotlib!
savefig('solution_%1.2f.png'%y0)
close()
