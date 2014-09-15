# Imports
import numpy as np
from functions1d.function1d import Function1D


# Problem
class GramacyLee(Function1D):
    """ Quadratic Function. """

    def __init__(self):
        """ Constructor. """
        # Meta Information
        self.min = np.array([0.0])
        self.value = 0.0
        self.domain = np.array([[0.5, 2.5]])
        self.smooth = True
        self.info = [True, False, False]
        self.latex_name = "Gramacy and Lee Function"
        self.latex_type = "Many Local Minima"
        self.latex_cost = "\[ f(x) = ... \]"
        self.latex_desc = "This is a simple one-dimensional test function. "

    def cost(self, x):
        """ Cost function. """
        # Cost
        cost = np.zeros(1)
        # Calculate Cost
        cost[0] = np.sin(10*np.pi*x[0])/(2*x[0]) + (x[0] - 1)**4
        # Return Cost
        return cost
