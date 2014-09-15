# Imports
import numpy as np
from numpy import exp, cos, sin, sqrt, pi
from functions2d.function2d import Function2D


# Problem
class Levi13(Function2D):
    """ Levi Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([1.0, 1.0])
        self.value = 0.0
        self.domain = np.array([[-10.0, 10.0], [-10.0, 10.0]])
        self.smooth = True
        self.info = [True, True, True]
        self.latex_name = "Levi No. 13"
        self.latex_type = "Many Local Minima"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "description"

    def cost(self, x):
        """ Cost function. """
        # Cost
        cost = (x[0] - 1)**2*(sin(3*pi*x[1])**2 + 1) + (x[1] - 1)**2*(sin(2*pi*x[1])**2 + 1) + sin(3*pi*x[0])**2
        # Return Cost
        return cost

    def grad(self, x):
        """ Grad function. """
        # Grads
        dx = (2*x[0] - 2)*(sin(3*pi*x[1])**2 + 1) + 6*pi*sin(3*pi*x[0])*cos(3*pi*x[0])
        dy = (2*x[0] - 2)*(sin(3*pi*x[1])**2 + 1) + 6*pi*sin(3*pi*x[0])*cos(3*pi*x[0])
        # Return Grad
        return np.array([dx, dy])

    def hess(self, x):
        """ Hess function. """
        # Grads
        dxx = -18*pi**2*sin(3*pi*x[0])**2 + 2*sin(3*pi*x[1])**2 + 18*pi**2*cos(3*pi*x[0])**2 + 2
        dxy = 6*pi*(2*x[0] - 2)*sin(3*pi*x[1])*cos(3*pi*x[1])
        dyy = 6*pi*(2*x[0] - 2)*sin(3*pi*x[1])*cos(3*pi*x[1])
        # Return Grad
        return np.array([[dxx, dxy], [dxy, dyy]])