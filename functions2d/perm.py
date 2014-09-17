# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class Perm(Function2D):
    """ Perm Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([1.0, 0.5])
        self.value = 0.0
        self.domain = np.array([[-2, 2], [-2, 2]])
        self.smooth = True
        self.info = [True, False, False]
        self.latex_name = "Perm Function"
        self.latex_type = "Bowl-Shaped"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "..."

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = np.sum([np.sum([(j + 1)*(x[j]**i - 1/(j**i)) for j in range(1, 3)]) for i in range(1, 3)])
        # Return Cost
        return c
