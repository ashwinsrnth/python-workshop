from pylab import *
import pandas as pd

x = linspace(0, 2, 50)
y = sin(x)
z = cos(x)

# Save the above to three columns of a LaTeX table:
df = pd.DataFrame({'$x$' : x, '$sin(x)' : y, '$cos(x)$' : z})
df.to_latex('data.tex')