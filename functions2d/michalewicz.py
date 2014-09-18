# Imports
import numpy as np
from numpy import exp, cos, sin, sqrt, pi
from functions2d.function2d import Function2D
from itertools import permutations


# Problem
class Michalewicz(Function2D):
    """ Michalewicz Function. """

    def __init__(self):
        """ Constructor. """
        # Constants
        self.m = 10
        # Information
        self.min = np.array([2.20, 1.57])
        self.value = -1.8013
        self.domain = np.array([[0, np.pi], [0, np.pi]])
        self.n = 2
        self.smooth = True
        self.info = [True, False, False]
        # Description
        self.latex_name = "Michalewicz"
        self.latex_type = "Steep"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "The Michalewicz function has d! local minima, and it is multimodal. "

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = -np.sum([np.sin(x[i])*sin(((i+1)*x[i]**2)/np.pi)**(2*self.m) for i in range(0, 2)], axis=0)
        # Return Cost
        return c