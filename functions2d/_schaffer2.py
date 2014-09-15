# Imports
import numpy as np
from problems.problems2d.problem2d import Problem2D


# Problem
class Schaffer2(Problem2D):
    """ Schaffer Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-100.0, -100.0], [-100.0, 100.0]])

    def cost(self, x):
        """ Cost function. """
        # Cost TODO
        cost = 0.0
        # Return Cost
        return cost

    def grad(self, x):
        """ Grad function. """
        # Grads TODO
        dx = 0.0
        dy = 0.0
        # Return Grad
        return np.array([dx, dy])

    def hess(self, x):
        """ Hess function. """
        # Grads TODO
        dxx = 0.0
        dxy = 0.0
        dyy = 0.0
        # Return Grad
        return np.array([[dxx, dxy], [dxy, dyy]])