# Imports
import numpy as np
from numpy import exp, cos, sin, sqrt, pi
from functions2d.function2d import Function2D


# Problem
class Shubert(Function2D):
    """ Shubert Function. """

    def __init__(self):
        """ Constructor. """
        # Information
        self.min = np.array([0.0, 0.0])
        self.value = -186.7309
        self.domain = np.array([[-5.12, 5.12], [-5.12, 5.12]])
        self.n = 2
        self.smooth = True
        self.info = [True, False, False]
        # Description
        self.latex_name = "Shubert Function"
        self.latex_type = "Many Local Minima"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "The Shubert function has several local minima and many global minima."

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = np.sum([i*np.cos((i+1)*x[0] + i) for i in range(1, 6)], axis=0)*np.sum([i*np.cos((i+1)*x[1] + i) for i in range(1, 6)], axis=0)
        # Return Cost
        return c