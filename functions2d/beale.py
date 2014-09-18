# Imports
import numpy as np
from numpy import exp, cos, sin, sqrt, pi
from functions2d.function2d import Function2D


# Problem
class Beale(Function2D):
    """ Beale's Function. """

    def __init__(self):
        """ Constructor. """
        # Information
        self.min = np.array([3.0, 0.5])
        self.value = 0.0
        self.domain = np.array([[-4.5, 4.5], [-4.5, 4.5]])
        self.n = 2
        self.smooth = True
        self.info = [True, True, True]
        # Description
        self.latex_name = "Beale Function"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "The Beale function is multimodal, with sharp peaks at the corners of the input domain. "

    def cost(self, x):
        """ Cost function. """
        # Cost
        cost = (1.5 - x[0] + x[0]*x[1])**2.0 + (2.25 - x[0] + x[0]*x[1]**2.0)**2.0 + (2.625 - x[0] + x[0]*x[1]**3.0)**2.0
        # Return Cost
        return cost

    def grad(self, x):
        """ Grad function. """
        # Grads
        dx = (2*x[1] - 2)*(x[0]*x[1] - x[0] + 1.5) + (2*x[1]**2 - 2)*(x[0]*x[1]**2 - x[0] + 2.25) + (2*x[1]**3 - 2)*(x[0]*x[1]**3 - x[0] + 2.625)
        dy = 6*x[0]*x[1]**2*(x[0]*x[1]**3 - x[0] + 2.625) + 4*x[0]*x[1]*(x[0]*x[1]**2 - x[0] + 2.25) + 2*x[0]*(x[0]*x[1] - x[0] + 1.5)
        # Return Grad
        return np.array([dx, dy])

    def hess(self, x):
        """ Hess function. """
        # Grads
        dxx = (x[1] - 1)*(2*x[1] - 2) + (x[1]**2 - 1)*(2*x[1]**2 - 2) + (x[1]**3 - 1)*(2*x[1]**3 - 2)
        dxy = 6*x[0]*x[1]**2*(x[1]**3 - 1) + 4*x[0]*x[1]*(x[1]**2 - 1) + 2*x[0]*x[1] + 2*x[0]*(x[1] - 1) - 2*x[0] + 6*x[1]**2*(x[0]*x[1]**3 - x[0] + 2.625) + 4*x[1]*(x[0]*x[1]**2 - x[0] + 2.25) + 3.0
        dyy = 18*x[0]**2*x[1]**4 + 8*x[0]**2*x[1]**2 + 2*x[0]**2 + 12*x[0]*x[1]*(x[0]*x[1]**3 - x[0] + 2.625) + 4*x[0]*(x[0]*x[1]**2 - x[0] + 2.25)
        # Return Grad
        return np.array([[dxx, dxy], [dxy, dyy]])