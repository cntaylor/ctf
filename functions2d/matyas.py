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
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = 0.26*x[0]**2 - 0.48*x[0]*x[1] + 0.26*x[1]**2
        # Return Cost
        return c

    def grad(self, x):
        """ Grad function. """
        # Grad
        g = np.zeros(x.shape)
        # Calculate Grads
        g[0] = 0.52*x[0] - 0.48*x[1]
        g[1] = -0.48*x[0] + 0.52*x[1]
        # Return Grad
        return g

    def hess(self, x):
        """ Hess function. """
        # Hess
        h = np.zeros((2, 2) + x.shape[1:])
        # Calculate Hess
        h[0][0] = 0.52
        h[0][1] = -0.48
        h[1][0] = h[0][1]
        h[1][1] = 0.52
        # Return Hess
        return h