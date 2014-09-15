# Imports
import numpy as np
from problems.problems2d.problem2d import Problem2D


# Problem
class StyblinskiTang(Problem2D):
    """ Schaffer Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([-2.903534*2.0, -2.903534*2.0])
        self.value = -39.16599*2.0
        self.domain = np.array([[-5.0, -5.0], [-5.0, 5.0]])

    def cost(self, x):
        """ Cost function. """
        # Cost
        cost = 0.5*(x[0]**4.0 - 16*x[0]**2.0 + 5.0*x[0] + x[1]**4.0 - 16*x[1]**2.0 + 5.0*x[1])
        # Return Cost
        return cost

    def grad(self, x):
        """ Grad function. """
        # Grads
        dx = -16.0*x[0]**1.0 + 2.0*x[0]**3.0 + 2.5
        dy = -16.0*x[1]**1.0 + 2.0*x[1]**3.0 + 2.5
        # Return Grad
        return np.array([dx, dy])

    def hess(self, x):
        """ Hess function. """
        # Grads
        dxx = 6.0*x[0]**2.0 - 16.0
        dxy = 0.0
        dyy = 6.0*x[1]**2.0 - 16.0
        # Return Grad
        return np.array([[dxx, dxy], [dxy, dyy]])