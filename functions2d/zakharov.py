# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class Zakharov(Function2D):
    """ Zakharov Function. """

    def __init__(self):
        """ Constructor. """
        # Information
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-5, 10.0], [-5, 10.0]])
        self.n = 2
        self.smooth = True
        self.info = [True, False, False]
        # Description
        self.latex_name = "Zakharov Function"
        self.latex_type = "Plate-Shaped"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "... "

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = np.sum([x[i]**2 for i in range(0, 2)], axis=0) + \
            np.sum([0.5*(i+1)*x[i] for i in range(0, 2)], axis=0)**2 + \
            np.sum([0.5*(i+1*x[i]) for i in range(0, 2)], axis=0)**4
        # Return Cost
        return c
