# Imports
import numpy as np
from numpy import exp, cos, sin, sqrt, pi
from functions2d.function2d import Function2D


# Problem
class Easom(Function2D):
    """ Matyas Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([pi, pi])
        self.value = -1
        self.domain = np.array([[-100.0, 100.0], [-100.0, 100.0]])
        self.latex_name = "Easom Function"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "The Easom function has several local minima. It is unimodal, and the global minimum has a " \
                          "small area relative to the search space. "

    def cost(self, x):
        """ Cost function. """
        # Cost
        cost = -exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*cos(x[0])*cos(x[1])
        # Return Cost
        return cost

    def grad(self, x):
        """ Grad function. """
        # Grads
        dx = -(-2*x[0] + 2*pi)*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*cos(x[0])*cos(x[1]) + exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*sin(x[0])*cos(x[1])
        dy = -(-2*x[1] + 2*pi)*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*cos(x[0])*cos(x[1]) + exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*sin(x[1])*cos(x[0])
        # Return Grad
        return np.array([dx, dy])

    def hess(self, x):
        """ Hess function. """
        # Grads
        dxx = -(-2*x[0] + 2*pi)**2*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*cos(x[0])*cos(x[1]) + 2*(-2*x[0] + 2*pi)*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*sin(x[0])*cos(x[1]) + 3*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*cos(x[0])*cos(x[1])
        dxy = -(-2*x[0] + 2*pi)*(-2*x[1] + 2*pi)*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*cos(x[0])*cos(x[1]) + (-2*x[0] + 2*pi)*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*sin(x[1])*cos(x[0]) + (-2*x[1] + 2*pi)*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*sin(x[0])*cos(x[1]) - exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*sin(x[0])*sin(x[1])
        dyy = -(-2*x[1] + 2*pi)**2*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*cos(x[0])*cos(x[1]) + 2*(-2*x[1] + 2*pi)*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*sin(x[1])*cos(x[0]) + 3*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)*cos(x[0])*cos(x[1])
        # Return Grad
        return np.array([[dxx, dxy], [dxy, dyy]])