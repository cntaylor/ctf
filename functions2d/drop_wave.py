# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class DropWave(Function2D):
    """ Matyas Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([0.0, 0.0])
        self.value = np.array([-1.0])
        self.domain = np.array([[-5.12, 5.12], [-5.12, 5.12]])
        self.smooth = True
        self.info = [True, False, False]
        self.latex_name = "Drop Wave Function"
        self.latex_type = "Many Local Minima"
        self.latex_cost = r'\[ f(x, y) = ... \]'
        self.latex_desc = "The Drop-Wave function is multimodal and highly complex."

    def cost(self, x):
        """ Cost function. """
        # Cost
        cost = np.zeros(1)
        # Calculate Cost
        cost[0] = -(1 + np.cos(12*np.sqrt(x[0]**2 + x[1]**2)))/(0.5*(x[0]**2 + x[1]**2) + 2)
        # Return Cost
        return cost

