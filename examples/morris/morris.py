import sys
sys.path.append('../..')

from SALib.sample.morris import Morris
from SALib.analyze import morris
from SALib.test_functions import Ishigami
import numpy as np

# Read the parameter range file and generate samples
param_file = '../../SALib/test_functions/params/Ishigami.txt'

# Files with a 4th column for "group name" will be detected automatically, e.g.:
# param_file = '../../SALib/test_functions/params/Ishigami_groups.txt'

# Generate samples
sample = Morris(param_file, samples=10000, num_levels=10, grid_jump=5, \
                      optimal_trajectories=None)

# To use optimized trajectories (brute force method), give an integer value for optimal_trajectories

# Save the parameter values in a file (they are needed in the analysis)
sample.save_data('model_input.txt')

# Run the "model" and save the output in a text file
# This will happen offline for external models
Y = Ishigami.evaluate(sample.get_inputs())
np.savetxt("model_output.txt", Y, delimiter=' ')

# Perform the sensitivity analysis using the model output
# Specify which column of the output file to analyze (zero-indexed)
Si = morris.analyze(param_file, 'model_input.txt', 'model_output.txt',
                    column=0, conf_level=0.95, print_to_console=True,
                    num_levels=10, grid_jump=5)
# Returns a dictionary with keys 'mu', 'mu_star', 'sigma', and 'mu_star_conf'
# e.g. Si['mu_star'] contains the mu* value for each parameter, in the
# same order as the parameter file
print(Si['mu_star'])
