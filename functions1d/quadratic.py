# Imports
import numpy as np
from functions1d.function1d import Function1D


# Problem
class Quadratic(Function1D):
    """ Quadratic Function. """

    def __init__(self):
        """ Constructor. """
        # Meta Information
        self.min = np.array([0.0])
        self.value = 0.0
        self.domain = np.array([[-np.inf, np.inf]])
        self.latex_name = "Quadratic Function"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "... "

    def cost(self, x):
        """ Cost function. """
        # Cost
        fx = x[0]**2.0
        # Return Cost
        return fx

    def grad(self, x):
        """ Grad function. """
        # Grads
        dx = 2.0*x[0]
        # Return Grad
        return np.array([dx])

    def hess(self, x):
        """ Hess function. """
        # Grads
        dxx = 2.0
        # Return Grad
        return np.array([[dxx]])
