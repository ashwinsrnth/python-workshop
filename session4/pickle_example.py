import pickle

# Here is a user defined type:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Create an object of type Point:
# with co-ordinates (3, 4)

p = Point(3, 4)

# Save the object to a "pickle"

with open('myPoint.pkl', 'w') as f:
    pickle.dump(p, f)


# Now, read the pickle file

with open('myPoint.pkl', 'r') as f:
    q = pickle.load(f)

# Test:

print q.x

# Always clean up after yourself:
import os
os.remove('myPoint.pkl')