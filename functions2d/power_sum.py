# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class PowerSum(Function2D):
    """ Power Sum Function. """

    def __init__(self):
        """ Constructor. """
        # Constants
        self.b = np.array([1,2])
        # Information
        self.min = np.array([2.0, 2.0])
        self.value = 0.0
        self.domain = np.array([[0, 2.0], [0, 2.0]])
        self.smooth = True
        self.info = [True, False, False]
        # Description
        self.latex_name = "Power Sum Function"
        self.latex_type = "Plate-Shaped"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "... "

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = np.sum([(np.sum([x[j]**(i+1) for j in range(0, 2)], axis=0) - self.b[i])**2 for i in range(0, 2)], axis=0)
        # Return Cost
        return c
