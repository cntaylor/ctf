# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class Booth(Function2D):
    """ Booth's Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([1.0, 3.0])
        self.value = 0.0
        self.domain = np.array([[-10.0, 10.0], [-10.0, 10.0]])
        self.smooth = True
        self.info = [True, True, True]
        self.latex_name = "Booth Function"
        self.latex_type = "Plate-Shaped"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "Plate shaped function."

    def cost(self, x):
        """ Cost function. """
        # Cost
        cost = np.zeros(1)
        # Calculate Cost
        cost[0] = (x[0] + 2.0*x[1] - 7.0)**2.0 + (2.0*x[0] + x[1] - 5.0)**2.0
        # Return Cost
        return cost

    def grad(self, x):
        """ Grad function. """
        # Grad
        grad = np.zeros(2)
        # Calculate Grads
        grad[0] = 2.0*(x[0] + 2.0*x[1] - 7.0) + 4.0*(2.0*x[0] + x[1] - 5.0)
        grad[1] = 4.0*(x[0] + 2.0*x[1] - 7.0) + 2.0*(2.0*x[0] + x[1] - 5.0)
        # Return Grad
        return grad

    def hess(self, x):
        """ Hess function. """
        # Hess
        hess = np.zeros(1)
        # Hesses
        hess[0][0] = 10.0
        hess[0][1] = 8.0
        hess[1][0] = hess[0][1]
        hess[1][1] = 10.0
        # Return Hess
        return hess