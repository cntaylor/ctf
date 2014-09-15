# Imports
import numpy as np
from numpy import exp, cos, sin, sqrt, pi
from functions2d.function2d import Function2D


# Problem
class McCormick(Function2D):
    """ McCormick Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([-0.54719, -1.54719])
        self.value = -1.9133
        self.domain = np.array([[-1.5, 4.0], [-3.0, 4.0]])
        self.smooth = True
        self.info = [True, True, True]
        self.latex_name = "McCormick Function"
        self.latex_type = "Plate-Shaped"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "description"

    def cost(self, x):
        """ Cost function. """
        # Cost
        cost = np.zeros(1)
        # Calculate Cost
        cost[0] = -1.5*x[0] + 2.5*x[1] + (x[0] - x[1])**2 + sin(x[0] + x[1]) + 1
        # Return Cost
        return cost

    def grad(self, x):
        """ Grad function. """
        # Grad
        grad = np.zeros(2)
        # Calculate Grads
        grad[0] = 2*x[0] - 2*x[1] + cos(x[0] + x[1]) - 1.5
        grad[1] = -2*x[0] + 2*x[1] + cos(x[0] + x[1]) + 2.5
        # Return Grad
        return grad

    def hess(self, x):
        """ Hess function. """
        # Hess
        hess = np.zeros(1)
        # Hesses
        hess[0][0] = -sin(x[0] + x[1]) + 2
        hess[0][1] = -sin(x[0] + x[1]) - 2
        hess[1][0] = hess[0][1]
        hess[1][1] = -sin(x[0] + x[1]) + 2
        # Return Hess
        return hess