from __future__ import division
import numpy as np
from ..util import read_param_file, scale_samples

class Sample(object):
    '''
    A template class, which all of the sample classes inherit.
    '''

    def __init__(self, parameter_file, samples):

        self.parameter_file = parameter_file
        pf = read_param_file(self.parameter_file)
        self.num_vars = pf['num_vars']
        self.bounds = pf['bounds']
        self.parameter_names = pf['names']
        self.samples = samples
        self.output_sample = None
        if pf['groups'] is not None:
            self.groups, self.group_names = pf['groups']
        else:
            self.groups, self.group_names = [None, None]


    def save_data(self, output, delimiter=' ', precision=8):
        '''
        Saves the data to a file for input into a model
        '''

        data_to_save = self.get_inputs()

        np.savetxt(output,
                   data_to_save,
                   delimiter=delimiter,
                   fmt='%.' + str(precision) + 'e')


    def get_inputs(self):
        '''
        Returns the scaled (according to the bounds from the parameter file)
        data as a numpy array
        '''
        scaled_samples = self.output_sample.copy()
        scale_samples(scaled_samples, self.bounds)
        return scaled_samples


    def get_inputs_unscaled(self):
        '''
        Returns the unscaled (according to the bounds from the parameter file)
        data as a numpy array
        '''
        return self.output_sample


    def parameter_names(self):
        return self.names
