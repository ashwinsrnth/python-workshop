# run_experiment.py

import subprocess
import numpy as np
import sys

init_conds = np.arange(1, 6, 1) # Solve for y0 = 1, 2, 3, 4, 5
for y0 in init_conds:
    ode = subprocess.Popen([sys.executable, "odesolve_cmd.py", str(y0)], stdout=subprocess.PIPE)
    ode.wait()
