from math import sin 

def f(x):
    try:
        return sin(x)
    except TypeError:
        err_msg = "An int or float is required"
        return err_msg

with open('errors.log', 'w') as e:
    print >>e, f('5')
