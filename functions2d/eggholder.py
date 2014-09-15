# Imports
import numpy as np
from numpy import exp, cos, sin, sqrt, pi
from functions2d.function2d import Function2D


# Problem
class Eggholder(Function2D):
    """ Eggholder Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([512, 404.2319])
        self.value = -959.6407
        self.domain = np.array([[-512.0, 512.0], [-512.0, 512.0]])
        self.smooth = True
        self.info = [True, False, False]
        self.latex_name = "Eggholder Function"
        self.latex_type = "Many Local Minima"
        self.latex_cost = r'\[ f(x,y) = - \left(y+47\right) \sin \left(\sqrt{\left|y + \frac{x}{2}+47\right|}\right) - x \sin \left(\sqrt{\left|x - \left(y + 47 \right)\right|}\right) \]'
        self.latex_desc = "The Eggholder function is a difficult function to optimize, because of the large number of local minima. "

    def cost(self, x):
        """ Cost function. """
        # Cost
        cost = np.zeros(1)
        # Calculate Cost
        cost[0] = -x[0]*sin(sqrt(abs(x[0] - x[1] - 47))) + (-x[1] - 47)*sin(sqrt(abs(x[0]/2 + x[1] + 47)))
        # Return Cost
        return cost