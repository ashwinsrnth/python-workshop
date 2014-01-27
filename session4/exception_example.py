from pylab import *

def print_to_file(L, f):

    try:        
        if f.mode != 'w':
            raise IOError

        if len(L) > 10:
            raise IndexError

        print >>f, L

    except IOError:
        print 'File must be opened in write mode!'

    except IndexError:
        print 'Length of list cannot exceed 10!'

L = [1, 2, 3]
f = open('ls.txt', 'w')
print_to_file(L, f)