# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class Sphere(Function2D):
    """ Sphere Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-np.inf, np.inf], [-np.inf, np.inf]])
        self.smooth = True
        self.info = [True, True, True]
        self.latex_name = "Sphere Function"
        self.latex_type = "Bowl-Shaped"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "It is continuous, convex and unimodal."

    def cost(self, x):
        """ Cost function. """
        # Cost
        cost = np.zeros(1)
        # Calculate Cost
        cost[0] = x[0]**2 + x[1]**2
        # Return Cost
        return cost

    def grad(self, x):
        """ Grad function. """
        # Grad
        grad = np.zeros(2)
        # Calculate Grads
        grad[0] = 2.0*x[0]
        grad[1] = 2.0*x[1]
        # Return Grad
        return grad

    def hess(self, x):
        """ Hess function. """
        # Hess
        hess = np.zeros(1)
        # Hesses
        hess[0][0] = 2.0
        hess[0][1] = 0.0
        hess[1][0] = hess[0][1]
        hess[1][1] = 2.0
        # Return Hess
        return hess