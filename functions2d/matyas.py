# Imports
import numpy as np
from numpy import exp, cos, sin, sqrt, pi
from functions2d.function2d import Function2D


# Problem
class Matyas(Function2D):
    """ Matyas Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-10.0, 10.0], [-10.0, 10.0]])
        self.smooth = True
        self.info = [True, True, True]
        self.latex_name = "Matyas Function"
        self.latex_type = "Plate-Shaped"
        self.latex_cost = "f(x,y) = ..."
        self.latex_desc = "This function..."

    def cost(self, x):
        """ Cost function. """
        # Cost
        cost = np.zeros(1)
        # Calculate Cost
        cost[0] = 0.26*x[0]**2 - 0.48*x[0]*x[1] + 0.26*x[1]**2
        # Return Cost
        return cost

    def grad(self, x):
        """ Grad function. """
        # Grad
        grad = np.zeros(2)
        # Calculate Grads
        grad[0] = 0.52*x[0] - 0.48*x[1]
        grad[1] = -0.48*x[0] + 0.52*x[1]
        # Return Grad
        return grad

    def hess(self, x):
        """ Hess function. """
        # Hess
        hess = np.zeros(1)
        # Hesses
        hess[0][0] = 0.52
        hess[0][1] = -0.48
        hess[1][0] = hess[0][1]
        hess[1][1] = 0.52
        # Return Hess
        return hess